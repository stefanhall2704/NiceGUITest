from nicegui import ui
from activity import Activity


class Task(Activity):
    def __init__(self, task_data):
        super().__init__(task_data.release_activity_task)

    def task_description(self) -> None:
        with ui.column():
            if self.activity.deployment_instructions:
                with ui.grid(columns=1):
                    ui.label("Description:")
                    ui.label(self.activity.deployment_instructions)

    def env_board_button(
        self, button_str: str, status, dialog=False, complete: bool = False
    ) -> None:
        if complete is False:
            ui.button(button_str, on_click=dialog.open).props(f"{status} color=green")
        else:
            ui.button(button_str).props(f"{status} color=green disabled")

    def dialog(self, text: str, button_str: str, status: str, complete: bool = False):
        if complete is False:
            with ui.dialog() as dialog, ui.card():
                ui.label(text)
                ui.button("Close", on_click=dialog.close)
            self.env_board_button(button_str=button_str, status=status, dialog=dialog)
        else:
            self.env_board_button(button_str=button_str, status=status, complete=True)

    def stage_board(self) -> None:
        stage_status = self.activity.stage_status.status
        with ui.column():
            ui.label(f"Stage Status: {stage_status}")

        if stage_status == "Not Started":
            self.dialog(
                text="Start Stage Task Dialog",
                button_str="Start Stage Task",
                status="inline",
            )
        elif stage_status == "In Progress":
            self.dialog(
                text="Complete Stage Task Dialog",
                button_str="Complete Stage Task",
                status="inline",
            )
        else:
            self.dialog(
                text="None", button_str="Completed", status="outline", complete=True
            )
