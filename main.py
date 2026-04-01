from src.image_builder import create_raw_image

from pathlib import Path

def init_runtime():
    base = Path.cwd()

    dirs = [
        base / "workspace",
        base / "workspace" / "mounted_image",
        base / "workspace" / "artifacts",
        base / "workspace" / "deleted_pool",
        base / "output",
        base / "output" / "images",
        base / "output" / "manifests",
        base / "logs",
        base / "temp"
    ]

    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)

    print("[+] Runtime environment ready")


def menu():
    print("\n=== DFIR Image Creator ===")
    print("1. Initialize Environment")
    print("2. Create Image (next step)")
    print("3. Seed Artifacts")
    print("4. Delete Artifacts")
    print("5. Finalize Image")
    print("0. Exit")


def main():
    while True:
        menu()
        choice = input("\nSelect option: ")

        if choice == "1":
            init_runtime()

        elif choice == "2":
            size = input("Enter image size (MB, default 100): ")
            size = int(size) if size else 100

            create_raw_image(size_mb=size)


        elif choice == "3":
            print("[*] Artifact seeding not implemented yet")

        elif choice == "4":
            print("[*] Deletion logic not implemented yet")

        elif choice == "5":
            print("[*] Finalization not implemented yet")

        elif choice == "0":
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()