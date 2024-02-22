from shiny import App, render, ui

# Define the user interface of your app
app_ui = ui.page_fluid(
    ui.input_text("name_input", "Enter your name:", placeholder="Type name here"),
    ui.output_text("greeting"),
)


# Define the server logic of your app
def server(input, output, session):
    @output
    @render.text
    def greeting():
        if input.name_input() == "":
            return "Hello, please enter your name above!"
        else:
            return f"Hello, {input.name_input()}!"


# Create the Shiny app
app = App(app_ui, server)

if __name__ == "__main__":
    app.run()
