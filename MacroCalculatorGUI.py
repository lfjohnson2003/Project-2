from tkinter import *
import MacroCalculatorFunctions


class GUI:
    def __init__(self, window):
        self.window = window

        self.frame_title = Frame(self.window)
        self.label_title = Label(self.frame_title, text='Macro Calculator\t')
        self.label_title.pack(side='top', padx=200)
        self.frame_title.pack(anchor='w', pady=10)

        self.frame_choice = Frame(self.window)
        self.label_choice = Label(self.frame_choice, text='Choose one\t')
        self.radio_1 = IntVar()
        self.radio_1.set(0)
        self.radio_cut = Radiobutton(self.frame_choice, text='Cut (lose weight)', variable=self.radio_1, value=1)
        self.radio_maintain = Radiobutton(self.frame_choice, text='Maintain', variable=self.radio_1, value=2)
        self.radio_bulk = Radiobutton(self.frame_choice, text='Bulk (gain weight)', variable=self.radio_1, value=3)
        self.label_choice.pack(side='left', padx=25)
        self.radio_cut.pack(side='left')
        self.radio_maintain.pack(side='left')
        self.radio_bulk.pack(side='left')
        self.frame_choice.pack(anchor='w', pady=5)

        self.frame_gender = Frame(self.window)
        self.label_gender = Label(self.frame_gender, text='Select gender\t')
        self.radio_2 = IntVar()
        self.radio_2.set(0)
        self.radio_male = Radiobutton(self.frame_gender, text='Male', variable=self.radio_2, value=1)
        self.radio_female = Radiobutton(self.frame_gender, text='Female', variable=self.radio_2, value=2)
        self.label_gender.pack(side='left', padx=25)
        self.radio_male.pack(side='left')
        self.radio_female.pack(side='left')
        self.frame_gender.pack(anchor='w', pady=5)

        self.frame_weight = Frame(self.window)
        self.label_weight = Label(self.frame_weight, text='Enter weight (in lbs)')
        self.entry_weight = Entry(self.frame_weight, width=33)
        self.label_weight.pack(padx=25, side='left')
        self.entry_weight.pack(padx=30, side='left')
        self.frame_weight.pack(anchor='w', pady=5)

        self.frame_height = Frame(self.window)
        self.label_height = Label(self.frame_height, text='Enter height (in inches)')
        self.entry_height = Entry(self.frame_height, width=33)
        self.label_height.pack(padx=25, side='left')
        self.entry_height.pack(padx=15, side='left')
        self.frame_height.pack(anchor='w', pady=5)

        self.frame_age = Frame(self.window)
        self.label_age = Label(self.frame_age, text='Enter age')
        self.entry_age = Entry(self.frame_age, width=40)
        self.label_age.pack(padx=25, side='left')
        self.entry_age.pack(padx=45, side='left')
        self.frame_age.pack(anchor='w', pady=5)

        self.frame_activity = Frame(self.window)
        self.label_activity = Label(self.frame_activity, text='Select activity level\t')
        self.radio_3 = IntVar()
        self.radio_3.set(0)
        self.radio_sedentary = Radiobutton(self.frame_activity, text='Sedentary', variable=self.radio_3, value=1)
        self.radio_light = Radiobutton(self.frame_activity, text='Light', variable=self.radio_3, value=2)
        self.radio_moderate = Radiobutton(self.frame_activity, text='Moderate', variable=self.radio_3, value=3)
        self.radio_very_active = Radiobutton(self.frame_activity, text='Very Active', variable=self.radio_3, value=4)
        self.label_activity.pack(side='left', padx=15)
        self.radio_sedentary.pack(side='left')
        self.radio_light.pack(side='left')
        self.radio_moderate.pack(side='left')
        self.radio_very_active.pack(side='left')
        self.frame_activity.pack(anchor='w', pady=5)

        self.frame_button = Frame(self.window)
        self.button_calculate = Button(self.frame_button, text='CALCULATE', command=self.compute)
        self.button_calculate.pack(anchor='w', pady=15)
        self.frame_button.pack()

        self.frame_result = Frame(self.window)
        self.label_result = Label(self.frame_result)
        self.label_result.pack(pady=10)
        self.frame_result.pack()

    def compute(self):
        try:
            choice = self.radio_1.get()
            gender = self.radio_2.get()
            weight = self.entry_weight.get()
            height = self.entry_height.get()
            age = self.entry_age.get()
            activity = self.radio_3.get()

            self.label_result.config(text=f'Macros \n Calorie Goal: '
                                     f'{MacroCalculatorFunctions.calories(choice, gender, weight, height, age, activity):.0f}'
                                     f' calories'
                                     f'\n Protein Goal: {MacroCalculatorFunctions.protein(weight):.0f}g'
                                     f'\n Fat Goal: {MacroCalculatorFunctions.fat(choice, gender, weight, height, age, activity):.0f}g'
                                     f'\n Carbs Goal: {MacroCalculatorFunctions.carbs(choice, gender, weight, height, age, activity):.0f}g')
            self.radio_1.set(0)
            self.radio_2.set(0)
            self.entry_weight.delete(0, END)
            self.entry_height.delete(0, END)
            self.entry_age.delete(0, END)
            self.radio_3.set(0)
        except ValueError:
            self.label_result.config(text='Enter numeric values')
        except:
            self.label_result.config(text='Error occurred! Check input values')
