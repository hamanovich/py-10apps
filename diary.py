import journal


def main():
    print_header()
    run_event_loop()


def print_header():
    print('JOURNAL APP')
    print('============')


def run_event_loop():
    cmd = 'EMPTY'
    journal_name = input('Name your journal (or `default`): ') or 'default'
    journal_data = journal.load(journal_name)

    print('What you want to do with your journal?')

    while cmd != 'x' and cmd:
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x' and cmd:
            print('Sorry, we don\'t understand \'{}\''.format(cmd))

    print('Done, goodbye!')
    journal.save(journal_name, journal_data)


def list_entries(data):
    print('Your journal entries:')
    entries = reversed(data)
    for i, entry in enumerate(entries):
        print('[{}] {}'.format(i + 1, entry))


def add_entry(data):
    text = input('Type your entry: ')
    journal.add_entry(text, data)


if __name__ == '__main__':
    main()
