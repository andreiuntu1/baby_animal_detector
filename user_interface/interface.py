import tkinter as tk
from baby_animal_detection.recording import audio_recorder

r = 0

def _increaseTemp():
    counter.set(counter.get() + 1)
    if (counter.get() in range(2, 10)):
        check_temp.set(check_temp.get() + 'It\'s a little too cold!\nCheck if someone is in the car!')
        prediction = audio_recorder.main(label_temp.get()+'°C in the car. It\'s a little too cold!\n')
        check_temp.set(check_temp.get() + prediction + '\n')
    if (counter.get() in range(0, 2)):
        check_temp.set(check_temp.get() + 'Now it\'s really cold!\n')
        prediction = audio_recorder.main(label_temp.get()+'°C in the car. Now it\'s really cold!\n')
        check_temp.set(check_temp.get() + prediction + '\n')
    if (counter.get() in range(-100, 0)):
        check_temp.set(check_temp.get() + 'Really, now I\'m freeazing!\n')
        prediction = audio_recorder.main(label_temp.get()+'°C in the car. Really, now I\'m freeazing!\n')
        check_temp.set(check_temp.get() + prediction + '\n')
    if (counter.get() in range(25, 29)):
        check_temp.set(check_temp.get() + 'It\'s getting warm!\n')
        prediction = audio_recorder.main(label_temp.get()+'°C in the car. It\'s getting warm!\n')
        check_temp.set(check_temp.get() + prediction + '\n')
    if (counter.get() in range(28, 30)):
        check_temp.set(check_temp.get() + 'It\'s getting pretty hot here!\n')
        prediction = audio_recorder.main(label_temp.get()+'°C in the car. It\'s getting pretty hot here!\n')
        check_temp.set(check_temp.get() + prediction + '\n')
    if (counter.get() in range(30, 100)):
        check_temp.set(check_temp.get() + 'It\'s really hot now!\n')
        prediction = audio_recorder.main(label_temp.get()+'°C in the car. It\'s really hot now!\n')
        check_temp.set(check_temp.get() + prediction + '\n')

def _decreaseTemp():
    counter.set(counter.get() - 1)
    if (counter.get() in range(5, 10)):
        check_temp.set(check_temp.get() + 'It\'s a little too cold!\nCheck if someone is in the car!')
        prediction = audio_recorder.main(label_temp.get()+'°C in the car. It\'s a little too cold!\n')
        check_temp.set(check_temp.get() + prediction + '\n')
    if (counter.get() in range(0, 5)):
        check_temp.set(check_temp.get() + 'Now it\'s really cold!\n')
        prediction = audio_recorder.main(label_temp.get()+'°C in the car. Now it\'s really cold!\n')
        check_temp.set(check_temp.get() + prediction + '\n')
    if (counter.get() in range(-100, 0)):
        check_temp.set(check_temp.get() + 'Really, now I\'m freeazing!\n')
        prediction = audio_recorder.main(label_temp.get()+'°C in the car. Really, now I\'m freeazing!\n')
        check_temp.set(check_temp.get() + prediction + '\n')
    if (counter.get() in range(25, 27)):
        check_temp.set(check_temp.get() + 'It\'s getting warm!\n')
        prediction = audio_recorder.main(label_temp.get()+'°C in the car. It\'s getting warm!\n')
        check_temp.set(check_temp.get() + prediction + '\n')
    if (counter.get() in range(27, 30)):
        check_temp.set(check_temp.get() + 'It\'s getting pretty hot here!\n')
        prediction = audio_recorder.main(label_temp.get()+'°C in the car. It\'s getting pretty hot here!\n')
        check_temp.set(check_temp.get() + prediction + '\n')
    if (counter.get() in range(30, 100)):
        check_temp.set(check_temp.get() + 'It\'s really hot now!\n')
        prediction = audio_recorder.main(label_temp.get()+'°C in the car. It\'s really hot now!\n')
        check_temp.set(check_temp.get() + prediction + '\n')

def process(event=None):
    content = label_temp.get() # get the contents of the entry widget
    if (int(content) in range(2, 5)):
        check_temp.set(check_temp.get() + 'It\'s a little too cold!\nCheck if someone is in the car!')
        prediction = audio_recorder.main(label_temp.get()+'°C in the car. It\'s a little too cold!\n')
        check_temp.set(check_temp.get() + prediction + '\n')
    if (int(content) in range(0, 2)):
        check_temp.set(check_temp.get() + 'Now it\'s really cold!\n')
        prediction = audio_recorder.main(label_temp.get()+'°C in the car. Now it\'s really cold!\n')
        check_temp.set(check_temp.get() + prediction + '\n')
    if (int(content) in range(-100, 0)):
        check_temp.set(check_temp.get() + 'Really, now I\'m freeazing!\n')
        prediction = audio_recorder.main(label_temp.get()+'°C in the car. Really, now I\'m freeazing!\n')
        check_temp.set(check_temp.get() + prediction + '\n')
    if (int(content) in range(25, 29)):
        check_temp.set(check_temp.get() + 'It\'s getting warm!\n')
        prediction = audio_recorder.main(label_temp.get()+'°C in the car. It\'s getting warm!\n')
        check_temp.set(check_temp.get() + prediction + '\n')
    if (int(content) in range(28, 30)):
        check_temp.set(check_temp.get() + 'It\'s getting pretty hot here!\n')
        prediction = audio_recorder.main(label_temp.get()+'°C in the car. It\'s getting pretty hot here!\n')
        check_temp.set(check_temp.get() + prediction + '\n')
    if (int(content) in range(30, 100)):
        check_temp.set(check_temp.get() + 'It\'s really hot now!\n')
        prediction = audio_recorder.main(label_temp.get()+'°C in the car. It\'s really hot now!\n')
        check_temp.set(check_temp.get() + prediction + '\n')

window = tk.Tk()
window.config(bg='white')
window.winfo_toplevel().title("Car Widget")
window.geometry("600x400")

#Temperature counter
counter = tk.IntVar()
counter.set(20)
frame = tk.LabelFrame(window)
frame.config(bg='#20ADE1')
frame.grid(row=0, columnspan=7, sticky='nsew',padx=5, pady=5, ipadx=10, ipady=70)
label_txt = tk.Label(frame, text = 'Car Temperature', font=("Courier", 17, "bold"),
                     foreground='#002b80', bg='#20ADE1').grid(row=0,sticky='E', padx=5, pady=2)
label_up = tk.Button(frame, text='^', command=_increaseTemp, fg="dark green", bg='#20ADE1').place(x=200, y=60)
label_down = tk.Button(frame, text="⌄", command=_decreaseTemp, fg="dark green", bg='#20ADE1').place(x=200, y=110)
label_temp = tk.Entry(frame, textvariable=counter, font=('Helvetica', 50), bg='#20ADE1', width=3)
label_celsius = tk.Label(frame, text='°C', font=('Helvetica', 50), bg='#20ADE1').place(x=110, y=65)

label_temp.place(x=15, y=65)
label_temp.bind('<Return>', process)


#record button
label_record = tk.Button(window, text='Record', command=lambda : audio_recorder.main("Check car!"), font=('Helvetica', 35)).place(x=25, y=250)

#log console
check_temp = tk.StringVar()
check_temp.set('Temperature from car is ok!\n')
row_nr = tk.IntVar()
row_nr.set(0)
log_frame = tk.LabelFrame(window)
log_frame.config(bg='black')
log_frame.grid(row=0, column=20, sticky='W', padx=50, pady=5, ipadx=130, ipady=170)
text_label = tk.Label(log_frame, textvariable=check_temp, foreground='white', background='black')
text_label1 = tk.Label(log_frame, textvariable=check_temp, foreground='white', background='black').grid(row=21,column=10, sticky="WE", pady=3,padx=5)

# def _check_temperature():
#     if (counter.get() in range(5, 21)):
#         color.set('#009900')
#         # return '#009900'
#         #label_celsius.configure(foreground='#009900')
#     if ((counter.get() in range(2,5)) or (counter.get() in range(21, 26))):
#         color.set('#e6e600')
#         # return '#e6e600'
#         label_celsius.configure(foreground='#e6e600')
#     if ((0 >= counter.get() < 2) or (counter.get() in range(26, 31))):
#         color.set('#ff9900')
#         # return '#ff9900'
#         # label_celsius.configure(foreground='#ff9900')
#     if (counter.get() in range(-100, 0) or (counter.get() in range(30, 100))):
#         color.set('#ff0000')
#         # return '#ff0000'
#         # label_celsius.configure(foreground='#ff0000')
window.mainloop()

