from tkinter import *
from ttkthemes import ThemedTk
from tkinter import ttk


class NumButton(ttk.Button):
    def __init__(self, master, number: int, column: int, row: int):
        super().__init__(master=master)
        self.root = master
        self.config(text=f'{number}', style='big.TButton', width=1,
                    command=lambda: self.add_to_display(number))
        self.grid(column=column, row=row)

    @staticmethod
    def add_to_display(number: int):
        current_display = display_buffer.get()
        if len(current_display) >= 14:
            return
        display_buffer.set(current_display + (str(number)))


class OperationButton(ttk.Button):
    def __init__(self, master, operation: str, column: int, row: int):
        super().__init__(master=master)
        self.root = master
        if operation == '=':
            self.config(text=operation, style='big.TButton', width=1,
                        command=lambda: equals())
        elif operation == 'C':
            self.config(text=operation, style='big.TButton', width=1,
                        command=lambda: clear())
        else:
            self.config(text=operation, style='big.TButton', width=1,
                        command=lambda: set_state(operation))
        self.grid(column=column, row=row)


def equals():
    global operation_buffer, state, display_buffer
    match state.get():
        case '+':
            display_buffer.set(str(int(display_buffer.get()) + operation_buffer))
            operation_buffer = 0
            state.set('')
        case '-':
            display_buffer.set(str(int(display_buffer.get()) - operation_buffer))
            operation_buffer = 0
            state.set('')
        case '*':
            display_buffer.set(str(int(display_buffer.get()) * operation_buffer))
            operation_buffer = 0
            state.set('')
        case '/':
            display_buffer.set(str(int(display_buffer.get()) / operation_buffer))
            operation_buffer = 0
            state.set('')


def clear():
    global operation_buffer, state, display_buffer
    operation_buffer = 0
    state.set('')
    display_buffer.set('')


def set_state(operation: str):
    global state, operation_buffer, display_buffer
    operation_buffer = int(display_buffer.get())
    display_buffer.set('')
    state.set(operation)


def create_buttons():
    buttons_frame = Frame(master=calculator)
    buttons_frame.pack(anchor='s')
    column = 0
    row = 1
    for number in range(0, 10):
        if number == 0:
            NumButton(buttons_frame, number, 2, 4)
            continue
        if column == 3:
            column = 0
            row += 1
        column += 1
        NumButton(buttons_frame, number, column, row)
    add_button = OperationButton(buttons_frame, '+', 4, 1)
    subtract_button = OperationButton(buttons_frame, '-', 4, 2)
    multiplier_button = OperationButton(buttons_frame, '*', 4, 3)
    divide_button = OperationButton(buttons_frame, '/', 4, 4)
    equals_button = OperationButton(buttons_frame, '=', 3, 4)
    clear_button = OperationButton(buttons_frame, 'C', 1, 4)


calculator = ThemedTk()
calculator.title('Calculator')
calculator.set_theme('alt')
style = ttk.Style()
style.configure('big.TButton', font=(None, 50))
style.configure('big.TLabel', font=(None, 75))
calculator.geometry('800x600')
# Display
display_frame = Frame(master=calculator)
display_frame.pack(anchor='n')
operation_buffer = 0
display_buffer = StringVar(master=display_frame)
state = StringVar()
screen = ttk.Label(master=display_frame, textvariable=display_buffer, style='big.TLabel')
screen.grid(column=1, row=0)
operation_label = ttk.Label(master=display_frame, textvariable=state, style='big.TLabel')
operation_label.grid(column=0, row=0)
create_buttons()


if __name__ == '__main__':
    calculator.mainloop()
