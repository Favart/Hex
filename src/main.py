from main.views.start import StartView

# Point d'entrée l'application

if __name__ == '__main__':

    current_vue = StartView()
    while current_vue:
        with open('assets/banner.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())
        current_vue.display_info()
        current_vue = current_vue.make_choice()

    with open('assets/over.txt', 'r', encoding="utf-8") as asset:
        print(asset.read())
