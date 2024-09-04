from tkinter import *
from tkinter import ttk, messagebox
import webbrowser



def search():
    if questionField.get() != "":
        if temp.get() == 'people':
            webbrowser.open(f'https://www.google.com/search?q={questionField.get()}')
            webbrowser.open(f'https://www.bing.com/search?q={questionField.get()}')
            webbrowser.open(f'https://www.ask.com/web?q={questionField.get()}')
            webbrowser.open(f'https://duckduckgo.com/?q={questionField.get()}')
            webbrowser.open(f'https://www.spokeo.com/{questionField.get()}')
        
        elif temp.get() == 'domain':
            webbrowser.open(f'https://www.statscrop.com/www/{questionField.get()}')
            #webbrowser.open(f'https://www.shodan.io/search?query={questionField.get()}')
            webbrowser.open(f'https://whois.domaintools.com/{questionField.get()}')
            webbrowser.open(f'https://sitereport.netcraft.com/?url={questionField.get()}')
            webbrowser.open(f'https://builtwith.com/{questionField.get()}')
            #webbrowser.open(f'https://securityheaders.com/q={questionField.get()}')
            webbrowser.open(f'https://www.criminalip.io/assets/search?query={questionField.get()}')
             
        elif temp.get() == 'ip':
            #webbrowser.open(f'https://whatismyipaddress.com/ip/{questionField.get()}')
            #webbrowser.open(f'https://www.whatismyip.com/{questionField.get()}')
            #webbrowser.open(f'https://iplocation.io/ip/{questionField.get()}')
            #webbrowser.open(f'https://ipinfo.io/{questionField.get()}')
            #webbrowser.open(f'https://dnschecker.org/ip-whois-lookup.php?query={questionField.get()}')
            #webbrowser.open(f'https://www.iplocation.net/search?cx=partner-pub-1026064395378929%3A2796854705&cof=FORID%3A10&ie=UTF-8&q={questionField.get()}')
            #webbrowser.open(f'https://www.shodan.io/host/{questionField.get()}')
            webbrowser.open(f'https://www.criminalip.io/asset/report/search?query={questionField.get()}') 
            #https://dnschecker.org/port-scanner.php?query=41.63.3.8&ptype=server
        else:
            messagebox.showerror('Error', 'Please search for people, domains, or IP addresses to view results in the browser.')



root = Tk()
root.geometry('660x400+150+150')
root.title('OSINT Community Central Web Crawler')
root.config(bg='#20879c')  # Set the background color to blue

temp = StringVar()
temp.set('people')

queryLabel = Label(root, text='Query', font=('Arial', 14, 'bold'), bg='#20879c')
queryLabel.grid(row=0, column=0)

questionField = Entry(root, width=45, font=('Arial', 14, 'bold'), bd=4, relief=SUNKEN)
questionField.grid(padx=10, row=0, column=1)

searchButton = Button(root, bd=0, cursor='hand2', bg='#20879c', activebackground='#1cefff', command=search)
searchButton.grid(row=0, column=3, padx=5)

googleRadioButton = ttk.Radiobutton(root, text='Search People', value='people', variable=temp)
googleRadioButton.place(x=75, y=40)

duckRadioButton = ttk.Radiobutton(root, text='Search Domains', value='domain', variable=temp)
duckRadioButton.place(x=255, y=40)

amazonRadioButton = ttk.Radiobutton(root, text='Search IP Address', value='ip', variable=temp)
amazonRadioButton.place(x=460, y=40)

def enter_function(event):
    searchButton.invoke()

root.bind('<Return>', enter_function)

root.mainloop()