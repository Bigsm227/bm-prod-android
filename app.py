from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup


class MonStudioApp(App):

    def build(self):
        # Conteneur principal avec espacement
        main_box = BoxLayout(
            orientation="vertical", padding=20, spacing=15
        )

        # Titre de l'application
        title_label = Label(
            text="BM PROD - GESTION STUDIO",
            font_size=20,
            bold=True,
            size_hint_y=None,
            height=50,
        )
        main_box.add_widget(title_label)

        # Bouton Formulaire
        btn_form = Button(
            text="📝 Enregistrer une prestation",
            size_hint_y=None,
            height=55,
            background_color=(0.1, 0.6, 0.4, 1),
        )
        btn_form.bind(on_press=self.action_formulaire)
        main_box.add_widget(btn_form)

        # Bouton Base Artistes / Impayés
        btn_base = Button(
            text="👥 Liste des Artistes & Soldes",
            size_hint_y=None,
            height=55,
            background_color=(0.2, 0.4, 0.8, 1),
        )
        btn_base.bind(on_press=self.action_base)
        main_box.add_widget(btn_base)

        return main_box

    def action_formulaire(self, instance):
        popup = Popup(
            title="Studio",
            content=Label(
                text="Ouverture du formulaire d'enregistrement..."
            ),
            size_hint=(None, None),
            size=(350, 200),
        )
        popup.open()

    def action_base(self, instance):
        popup = Popup(
            title="Studio",
            content=Label(text="Ouverture de la base des artistes..."),
            size_hint=(None, None),
            size=(350, 200),
        )
        popup.open()


if __name__ == "__main__":
    MonStudioApp().run()