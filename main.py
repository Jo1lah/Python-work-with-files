from utils.storage import load_notes, save_notes
from utils.notes_service import show_notes, toggle_done, add_note, delete_notes

notes = load_notes()

while True:
    print("\n1. Показать")
    print("2. Добавить")
    print("3. Переключить done")
    print("5. Удалить заметку")
    print("4. Сохранить")
    print("0. Выход")

    choice = input("Выбор: ")

    if choice == "1":
        show_notes(notes)
    elif choice == "2":
        add_note(notes)
    elif choice == "3":
        toggle_done(notes)
    elif choice == "4":
        save_notes(notes)
        print("Сохранено")
    elif choice == "5":
        delete_notes(notes)
    elif choice == "0":
        save_notes(notes)
        print("Выход")
        break
    else:
        print("Неверный выбор")