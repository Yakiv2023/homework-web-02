from prettytable import PrettyTable

notes = []

def add_note():
    # Додавання нотатки
    title = input('Enter a title for the note: ')
    content = input('Enter the note text: ')
    tags = input(
        'Enter tags for the note (comma-separated, press Enter to skip): ')

    if tags:
        tags = [tag.strip() for tag in tags.split(',')]

    note = {'title': title, 'content': content, 'tags': tags}
    notes.append(note)
    save_notes()
    print('Note successfully added and saved!')

def edit_note():
    # Редагування нотатки
    title = input('Enter the title of the note to edit: ')
    note_found = False

    for note in notes:
        if note['title'] == title:
            new_title = input('Enter a new title for the note: ')
            new_content = input('Enter new note text: ')
            new_tags = input(
                'Enter new tags for the note (comma-separated, press Enter to skip): ')

            if new_tags:
                new_tags = [tag.strip() for tag in new_tags.split(',')]

            note['title'] = new_title
            note['content'] = new_content
            note['tags'] = new_tags
            note_found = True
            break

    if note_found:
        save_notes()
        print('Note successfully edited and saved!')
    else:
        print('No note with this title was found.')

def delete_note():
    # Видалення нотатки
    title = input('Enter the title of the note to delete: ')
    note_found = False

    for note in notes:
        if note['title'] == title:
            notes.remove(note)
            note_found = True
            break

    if note_found:
        save_notes()
        print('Note successfully deleted!')
    else:
        print('No note with this title was found.')

def search_notes():
    # Пошук нотаток
    keyword = input('Enter a keyword to search: ')
    if found_notes := [
        note
        for note in notes
        if keyword.lower() in note['title'].lower()
        or keyword.lower() in note['content'].lower()
        or keyword.lower() in [x.lower() for x in note['tags']]
    ]:
        table = PrettyTable(['Title', 'Text', 'Tags'])
        for note in found_notes:
            table.add_row([note['title'], note['content'], note['tags']])
        print(table)
    else:
        print('No notes found.')

def sort_notes_by_tag():
    # Сортування нотаток за тегами
    tags = set()
    for note in notes:
        if note['tags']:
            tags.update(note['tags'])
    tags_list = list(tags)

    table = PrettyTable(['Tag Number', 'Tag'])
    for i, tag in enumerate(tags_list):
        table.add_row([i + 1, tag])
    print(table)

    choice = input('Enter the tag number to sort notes: ')
    if choice.isdigit() and int(choice) in range(1, len(tags_list) + 1):
        tag = tags_list[int(choice) - 1]
        sorted_notes = [note for note in notes if note['tags']
                        and tag.lower() in [t.lower() for t in note['tags']]]
        if sorted_notes:
            table = PrettyTable(['Title', 'Text', 'Tags'])
            for note in sorted_notes:
                table.add_row([note['title'], note['content'],
                               ', '.join(note['tags'])])
            print('Sorted notes:')
            print(table)
        else:
            print('No notes found with this tag.')
    else:
        print('Invalid tag number.')

def save_notes():
    # Збереження нотаток у файл
    with open('notes.txt', 'w') as file:
        for note in notes:
            file.write(f"Title: {note['title']}\n")
            file.write(f"Text: {note['content']}\n")
            if note['tags']:
                file.write(f"Tags: {', '.join(note['tags'])}\n")
            file.write('\n')

def load_notes():
    # Завантаження нотаток з файлу
    notes.clear()
    try:
        with open('notes.txt', 'r') as file:
            lines = file.readlines()
            title = ''
            content = ''
            tags = []

            for line in lines:
                if line.startswith('Title: '):
                    title = line[7:].strip()
                elif line.startswith('Text: '):
                    content = line[6:].strip()
                elif line.startswith('Tags: '):
                    tags = [tag.strip() for tag in line[6:].split(',')]
                elif line == '\n':
                    note = {'title': title, 'content': content, 'tags': tags}
                    notes.append(note)
                    title = ''
                    content = ''
                    tags = []
    except FileNotFoundError:
        pass

def notes_menu():
    table = PrettyTable(['Command', 'Instruction'])
    table.add_rows(
        [
            ["1", "Add a note"],
            ["2", "Edit note"],
            ["3", "Delete note"],
            ["4", "Search notes"],
            ["5", "Sort notes by tags"],
            ["6", "Exit the notes"],
        ]
    )

    while True:
        print("\nNotes Menu:")
        print(table)
        command = input("Enter command the command number: ")

        if command == "1":
            add_note()
        elif command == "2":
            edit_note()
        elif command == "3":
            delete_note()
        elif command == "4":
            search_notes()
        elif command == "5":
            sort_notes_by_tag()
        elif command == "6":
            break
        else:
            print("Invalid command.")

def main():
    load_notes()
    notes_menu()

if __name__ == "__main__":
    main()
