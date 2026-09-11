from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup


class BMProdApp(App):

    def build(self):
        main_box = BoxLayout(
            orientation="vertical", padding=20, spacing=15
        )

        title_label = Label(
            text="BM PROD - OFFICIEL",
            font_size=22,
            bold=True,
            size_hint_y=None,
            height=50,
        )
        main_box.add_widget(title_label)

        btn_form = Button(
            text="📝 Réserver une session studio",
            size_hint_y=None,
            height=55,
            background_color=(0.1, 0.6, 0.4, 1),
        )
        btn_form.bind(on_press=self.action_reservation)
        main_box.add_widget(btn_form)

        btn_store = Button(
            text="🎵 Catalogue d'Instrumentales",
            size_hint_y=None,
            height=55,
            background_color=(0.2, 0.4, 0.8, 1),
        )
        btn_store.bind(on_press=self.action_store)
        main_box.add_widget(btn_store)

        return main_box

    def action_reservation(self, instance):
        popup = Popup(
            title="Réservation Studio",
            content=Label(
                text="Module de réservation MyNita / Amanata en cours..."
            ),
            size_hint=(None, None),
            size=(350, 200),
        )
        popup.open()

    def action_store(self, instance):
        popup = Popup(
            title="Boutique Beats",
            content=Label(text="Chargement des instrumentales..."),
            size_hint=(None, None),
            size=(350, 200),
        )
        popup.open()


if __name__ == "__main__":
    BMProdApp().run()
