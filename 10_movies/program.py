import requests.exceptions

from movie_client import MovieClient


def main():
    print_header()
    search_event_loop()


def print_header():
    print('MOVIES SEARCH APP')
    print('=================')


def search_event_loop():
    search = None

    while search != 'x':
        try: 
            search = input('What are you seeking (x for exit): ')

            if search != 'x':
                client = MovieClient(search)
                results = client.perform_search()

                print('Found {} results'.format(len(results)))

                for r in results:
                    print('{} --- {}'.format(r.Year, r.Title))

        except requests.exceptions.ConnectionError as ce:
            print('ERROR: Network is down.')
        except KeyError as ve:
            print('ERROR: Search string is invalid {}'.format(ve))
        except Exception as x:
            print('Ah, something goes wrong. ERROR: {}'.format(x))

    print('exiting…')


if __name__ == "__main__":
    main()
