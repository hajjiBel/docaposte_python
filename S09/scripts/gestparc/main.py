# main.py – GestParc, étape 6 (Séance 9)
# Hiérarchie d'équipements : Equipment (abstraite) -> Laptop, Server, Printer, NetworkDevice.

from abc import ABC, abstractmethod

APP_NAME = "GestParc"
APP_VERSION = "0.7.0"
CURRENT_YEAR = 2026


class NetworkMixin:
    """Ajoute une adresse IP gérée à un équipement réseau."""

    _ip_address: str | None = None

    @staticmethod
    def is_valid_ip(ip: str) -> bool:
        """Vérifie le format d'une adresse IPv4."""
        parts = ip.split(".")
        return len(parts) == 4 and all([p.isdigit() and 0 <= int(p) <= 255 for p in parts])

    @property
    def ip_address(self) -> str | None:
        return self._ip_address

    @ip_address.setter
    def ip_address(self, value: str | None) -> None:
        if value is not None and not self.is_valid_ip(value):
            print(f"Adresse IP refusée : {value}")
            return
        self._ip_address = value


class Equipment(ABC):
    """Équipement du parc informatique (classe abstraite)."""

    CATEGORY = "equipment"
    PREFIX = "EQ"
    count = 0

    def __init__(self, asset_tag: str, brand: str, model: str, purchase_year: int,
                 price: float, assigned_to: str | None = None) -> None:
        self.asset_tag = asset_tag.upper()
        self.brand = brand
        self.model = model
        self.purchase_year = purchase_year
        self._price = 0.0
        self.price = price
        self._assigned_to = assigned_to
        Equipment.count += 1

    # --- Méthodes abstraites : chaque sous-classe DOIT les définir
    @abstractmethod
    def maintenance_interval_months(self) -> int:
        """Périodicité de maintenance préventive, en mois."""

    @abstractmethod
    def specs(self) -> str:
        """Caractéristiques techniques propres au type d'équipement."""

    # --- Méthodes communes
    @property
    def category(self) -> str:
        return self.CATEGORY

    @staticmethod
    def is_valid_tag(tag: str) -> bool:
        return len(tag) == 6 and tag[:2].isalpha() and tag[2] == "-" and tag[3:].isdigit()

    def has_expected_prefix(self) -> bool:
        return self.asset_tag.startswith(self.PREFIX + "-")

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        if float(value) < 0:
            print(f"Prix refusé pour {self.asset_tag} : {value}")
            return
        self._price = float(value)

    @property
    def assigned_to(self) -> str | None:
        return self._assigned_to

    def age(self, current_year: int) -> int:
        return current_year - self.purchase_year

    def is_available(self) -> bool:
        return self._assigned_to is None

    def assign(self, employee: str) -> bool:
        if not self.is_available():
            return False
        self._assigned_to = employee
        return True

    def unassign(self) -> None:
        self._assigned_to = None

    def to_dict(self) -> dict:
        return {"asset_tag": self.asset_tag, "category": self.category, "brand": self.brand,
                "model": self.model, "purchase_year": self.purchase_year, "price": self.price,
                "assigned_to": self.assigned_to}

    def __str__(self) -> str:
        name = f"{self.brand} {self.model}"
        return (f"{self.asset_tag:<7} | {self.category:<8} | {name:<25} | "
                f"{self.price:>10,.2f} DT | {self.assigned_to or '-'}")

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.asset_tag!r}, {self.brand!r}, {self.model!r})"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Equipment) and self.asset_tag == other.asset_tag

    def __lt__(self, other: "Equipment") -> bool:
        return self.asset_tag < other.asset_tag


class Laptop(Equipment):
    """Ordinateur portable."""

    CATEGORY = "laptop"
    PREFIX = "LT"

    def __init__(self, asset_tag: str, brand: str, model: str, purchase_year: int, price: float,
                 assigned_to: str | None = None, *, ram_gb: int = 16, screen_inches: float = 14.0) -> None:
        super().__init__(asset_tag, brand, model, purchase_year, price, assigned_to)
        self.ram_gb = ram_gb
        self.screen_inches = screen_inches

    def maintenance_interval_months(self) -> int:
        return 24

    def specs(self) -> str:
        return f"{self.ram_gb} Go RAM, écran {self.screen_inches}\""

    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update(ram_gb=self.ram_gb, screen_inches=self.screen_inches)
        return data


class Server(NetworkMixin, Equipment):
    """Serveur physique."""

    CATEGORY = "server"
    PREFIX = "SV"

    def __init__(self, asset_tag: str, brand: str, model: str, purchase_year: int, price: float,
                 assigned_to: str | None = None, *, cpu_count: int = 16, ram_gb: int = 64,
                 rack: str = "R1", ip_address: str | None = None) -> None:
        super().__init__(asset_tag, brand, model, purchase_year, price, assigned_to)
        self.cpu_count = cpu_count
        self.ram_gb = ram_gb
        self.rack = rack
        self.ip_address = ip_address

    def maintenance_interval_months(self) -> int:
        return 6

    def specs(self) -> str:
        return f"{self.cpu_count} cœurs, {self.ram_gb} Go RAM, baie {self.rack}, IP {self.ip_address or '-'}"

    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update(cpu_count=self.cpu_count, ram_gb=self.ram_gb, rack=self.rack, ip_address=self.ip_address)
        return data


class Printer(NetworkMixin, Equipment):
    """Imprimante réseau."""

    CATEGORY = "printer"
    PREFIX = "PR"

    def __init__(self, asset_tag: str, brand: str, model: str, purchase_year: int, price: float,
                 assigned_to: str | None = None, *, is_color: bool = False, pages_printed: int = 0,
                 ip_address: str | None = None) -> None:
        super().__init__(asset_tag, brand, model, purchase_year, price, assigned_to)
        self.is_color = is_color
        self.pages_printed = pages_printed
        self.ip_address = ip_address

    def maintenance_interval_months(self) -> int:
        # Une imprimante très sollicitée est entretenue plus souvent
        return 3 if self.pages_printed > 50_000 else 12

    def specs(self) -> str:
        return f"{'couleur' if self.is_color else 'monochrome'}, {self.pages_printed:,} pages, IP {self.ip_address or '-'}"

    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update(is_color=self.is_color, pages_printed=self.pages_printed, ip_address=self.ip_address)
        return data


class NetworkDevice(NetworkMixin, Equipment):
    """Équipement réseau (switch, routeur, point d'accès)."""

    CATEGORY = "network"
    PREFIX = "SW"

    def __init__(self, asset_tag: str, brand: str, model: str, purchase_year: int, price: float,
                 assigned_to: str | None = None, *, port_count: int = 24,
                 ip_address: str | None = None) -> None:
        super().__init__(asset_tag, brand, model, purchase_year, price, assigned_to)
        self.port_count = port_count
        self.ip_address = ip_address

    def maintenance_interval_months(self) -> int:
        return 12

    def specs(self) -> str:
        return f"{self.port_count} ports, IP {self.ip_address or '-'}"

    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update(port_count=self.port_count, ip_address=self.ip_address)
        return data


EQUIPMENT_TYPES: dict[str, type[Equipment]] = {
    cls.CATEGORY: cls for cls in (Laptop, Server, Printer, NetworkDevice)
}


def equipment_from_dict(data: dict) -> Equipment:
    """Fabrique : crée l'objet de la bonne sous-classe à partir d'un dictionnaire."""
    cls = EQUIPMENT_TYPES[data["category"]]
    common = ["asset_tag", "brand", "model", "purchase_year", "price", "assigned_to"]
    specific = {k: v for k, v in data.items() if k not in common and k != "category"}
    return cls(data["asset_tag"], data["brand"], data["model"], data["purchase_year"],
               data["price"], data.get("assigned_to"), **specific)


class Employee:
    """Employé pouvant recevoir des équipements."""

    def __init__(self, first_name: str, last_name: str, department: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.department = department

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return f"{self.full_name} ({self.department})"


class Inventory:
    """Inventaire du parc informatique."""

    def __init__(self) -> None:
        self._items: list[Equipment] = []

    def add(self, equipment: Equipment) -> bool:
        if (not isinstance(equipment, Equipment)
                or not Equipment.is_valid_tag(equipment.asset_tag)
                or equipment in self._items):
            return False
        self._items.append(equipment)
        return True

    def find(self, asset_tag: str) -> Equipment | None:
        tag = asset_tag.upper()
        for equipment in self._items:
            if equipment.asset_tag == tag:
                return equipment
        return None

    def assign(self, asset_tag: str, employee: Employee) -> bool:
        equipment = self.find(asset_tag)
        return equipment is not None and equipment.assign(employee.full_name)

    def by_type(self, cls: type) -> list[Equipment]:
        """Équipements instances d'une classe donnée (sous-classes comprises)."""
        return [e for e in self._items if isinstance(e, cls)]

    def stats(self) -> dict[str, int]:
        result: dict[str, int] = {}
        for equipment in self._items:
            result[equipment.category] = result.get(equipment.category, 0) + 1
        return result

    def total_value(self, category: str | None = None) -> float:
        return sum([e.price for e in self._items if category is None or e.category == category])

    def available(self) -> list[Equipment]:
        return [e for e in self._items if e.is_available()]

    def older_than(self, years: int, current_year: int) -> list[Equipment]:
        return [e for e in self._items if e.age(current_year) >= years]

    def maintenance_plan(self) -> list[tuple[str, int]]:
        """Polymorphisme : chaque équipement donne sa propre périodicité."""
        return sorted([(e.asset_tag, e.maintenance_interval_months()) for e in self._items],
                      key=lambda item: item[1])

    def ip_plan(self) -> dict[str, str | None]:
        """Adresses IP des équipements réseau (ceux qui ont le mixin)."""
        return {e.asset_tag: e.ip_address for e in self._items if isinstance(e, NetworkMixin)}

    def __len__(self) -> int:
        return len(self._items)

    def __contains__(self, item: object) -> bool:
        if isinstance(item, str):
            return self.find(item) is not None
        return item in self._items

    def __getitem__(self, index: int) -> Equipment:
        return self._items[index]


def demo_inventory() -> Inventory:
    """Inventaire de démonstration."""
    inventory = Inventory()
    inventory.add(Server("SV-001", "HPE", "ProLiant DL380", 2019, 18500, cpu_count=32, ram_gb=256,
                         rack="R2", ip_address="10.0.0.10"))
    inventory.add(Laptop("LT-001", "Dell", "Latitude 5440", 2023, 3200, "Amira Ben Salah", ram_gb=32))
    inventory.add(Printer("PR-001", "HP", "LaserJet M404", 2021, 950, pages_printed=62_000,
                          ip_address="10.0.2.50"))
    inventory.add(NetworkDevice("SW-001", "Cisco", "Catalyst 9200", 2020, 4100, port_count=48,
                                ip_address="10.0.0.2"))
    return inventory


def main() -> None:
    """Menu console."""
    inventory = demo_inventory()
    print(f"{APP_NAME} v{APP_VERSION} – {len(inventory)} équipements")
    while True:
        print("\n1. Lister  2. Détails  3. Statistiques  4. Plan de maintenance  5. Plan IP  0. Quitter")
        choice = input("Votre choix : ").strip()
        if choice == "0":
            break
        if choice == "1":
            for equipment in sorted(inventory):
                print(equipment)
        elif choice == "2":
            equipment = inventory.find(input("Numéro : "))
            print(f"{equipment!r} : {equipment.specs()}" if equipment else "Introuvable")
        elif choice == "3":
            for category, count in inventory.stats().items():
                print(f"{category:<8} : {count:>3}  ({inventory.total_value(category):,.2f} DT)")
        elif choice == "4":
            for tag, months in inventory.maintenance_plan():
                print(f"{tag} : tous les {months} mois")
        elif choice == "5":
            for tag, ip in inventory.ip_plan().items():
                print(f"{tag} : {ip}")
        else:
            print("Choix invalide")


main()
