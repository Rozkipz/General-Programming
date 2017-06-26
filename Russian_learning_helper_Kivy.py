# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import pygame
import time
import sys
import hashlib
import random
import csv
import fileinput
import kivy

kivy.require('1.1.3')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.layout import Layout
from kivy.config import Config
from kivy.core.audio import SoundLoader


class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 1
        self.padding = 100
        self.spacing = 20
        self.add_widget(Label(text='Welcome to the Russian Language Aid!'))
        self.btrn1 = Button(text='Press to continue')
        self.btrn1.bind(on_press=self.Menu)
        self.add_widget(self.btrn1)

    def Menu(self, *args):
        self.clear_widgets()
        self.cols = 2
        self.Userlabel = (Label(text='User Name'))
        self.add_widget(self.Userlabel)
        self.UserName = TextInput(multiline=False)
        self.add_widget(self.UserName)
        self.Passlabel = Label(text='Password')
        self.add_widget(self.Passlabel)
        self.PassWord = TextInput(password=True, multiline=False)
        self.add_widget(self.PassWord)
        self.Blank = Label(text='\n')
        self.Blank2 = Label(text='\n')
        self.add_widget(self.Blank)
        self.add_widget(self.Blank2)
        self.btrn1 = Button(text='Create Account')
        self.btrn1.bind(on_press=lambda x=self.CreateAccount: self.CreateAccount())
        self.add_widget(self.btrn1)
        self.btrn2 = Button(text='Log in')
        self.add_widget(self.btrn2)
        self.btrn2.bind(on_press=lambda x=self.readUser: self.readUser(self.UserName.text, self.PassWord.text))

    def CreateAccount(self, *args):
        self.clear_widgets()
        self.cols = 2
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='Password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)
        self.add_widget(Label(text='\n'))
        self.add_widget(Label(text='\n'))
        self.btrn5 = Button(text='Create Account')
        self.btrn5.bind(on_press=lambda x=self.username.text, y=self.password.text: self.createUser(self.username.text,
                                                                                                    self.password.text))
        self.add_widget(self.btrn5)
        self.btrn6 = Button(text='Return to menu')
        self.btrn6.bind(on_press=self.Menu)
        self.add_widget(self.btrn6)

    def UserExist(self, *args):
        self.clear_widgets()
        self.cols = 1
        self.add_widget(Label(text='That username already exists, please pick another'))
        self.add_widget(Label(text='\n'))
        self.btrn1 = Button(text='Try again')
        self.btrn1.bind(on_press=self.CreateAccount)
        self.add_widget(self.btrn1)
        self.btrn2 = Button(text='Back to Menu')
        self.btrn2.bind(on_press=self.Menu)
        self.add_widget(self.btrn2)

    def MainMenu(self, *args):
        self.clear_widgets()
        self.cols = 1
        self.btrn1 = Button(text='Listen To Words')
        self.btrn1.bind(on_press=self.SortPage)
        self.add_widget(self.btrn1)
        self.btrn2 = Button(text='Test Yourself')
        self.btrn2.bind(on_press=self.Test)
        self.add_widget(self.btrn2)
        self.btrn3 = Button(text='Reset Your Progress')
        self.add_widget(self.btrn3)
        self.btrn3.bind(on_press=self.Reset1)
        self.add_widget(Label(text='\n'))
        self.btrn4 = Button(text='Log Out')
        self.btrn4.bind(on_press=self.Menu)
        self.add_widget(self.btrn4)

    def Reset1(self, *args):
        self.clear_widgets()
        self.cols = 3
        self.add_widget(Label(text='\n'))
        self.add_widget(Label(text='Are you sure you want to delete your progress?'))
        self.add_widget(Label(text='\n'))
        self.btrn1 = Button(text='Yes')
        self.btrn1.bind(on_press=self.Reset2)
        self.add_widget(self.btrn1)
        self.add_widget(Label(text='\n'))
        self.btrn2 = Button(text='No')
        self.btrn2.bind(on_press=self.Reset3)
        self.add_widget(self.btrn2)

    def Reset2(self, *args):
        self.clear_widgets()
        self.cols = 1
        createWordBoxes(MP3Files, X)
        self.add_widget(Label(text='Your progress has been reset'))
        self.add_widget(Label(text='\n'))
        self.add_widget(Label(text='\n'))
        self.btrn1 = Button(text='Return to menu')
        self.btrn1.bind(on_press=self.Menu)
        self.add_widget(self.btrn1)

    def Reset3(self, *args):
        self.clear_widgets()
        self.cols = 1
        self.add_widget(Label(text='Your progress has not been reset'))
        self.add_widget(Label(text='\n'))
        self.add_widget(Label(text='\n'))
        self.btrn1 = Button(text='Return to menu')
        self.btrn1.bind(on_press=self.MainMenu)
        self.add_widget(self.btrn1)

    def SortPage(self, *args):
        self.clear_widgets()
        self.rows = 6
        Num = 0
        self.btrn1 = Button(text='Sort alphabetically (English)')
        self.btrn1.bind(on_press=lambda btn=None, x=self.btrn1, Num1=Num: self.WordTie(btn, x.text, Num1))
        self.add_widget(self.btrn1)
        self.btrn2 = Button(text='Sort alphabetically (Russian)')
        self.btrn2.bind(on_press=lambda btn=None, x=self.btrn2, Num1=Num: self.WordTie(btn, x.text, Num1))
        self.add_widget(self.btrn2)
        self.btrn3 = Button(text='Sort by word length (English)')
        self.btrn3.bind(on_press=lambda btn=None, x=self.btrn3, Num1=Num: self.WordTie(btn, x.text, Num1))
        self.add_widget(self.btrn3)
        self.btrn4 = Button(text='Sort by word length (Russian)')
        self.btrn4.bind(on_press=lambda btn=None, x=self.btrn4, Num1=Num: self.WordTie(btn, x.text, Num1))
        self.add_widget(self.btrn4)
        self.add_widget(Label(text='\n'))
        self.btrn5 = Button(text='Return to menu')
        self.btrn5.bind(on_press=self.MainMenu)
        self.add_widget(self.btrn5)

    def PlayMp3File(self, btn, path, *args):
        print path
        pygame.mixer.init()
        pygame.mixer.music.load(("I:\\" + path))
        pygame.mixer.music.play()

    def GetAttributes(self, L, RUS, word, *args):
        if RUS:
            for item in MP3Files:
                if word[L] == item.russian:
                    Path = item.path
                    Eng = item.english
                    Rus = item.russian
                    Length = item.length
        elif not RUS:
            for item in MP3Files:
                if word[L] == item.english:
                    Path = item.path
                    Eng = item.english
                    Rus = item.russian
                    Length = item.length
        return Path, Eng, Rus, Length

    def RusOrEng(self, y, *args):
        word = []
        if y == 'Sort alphabetically (Russian)':
            for rus in sortingrus(MP3Files):
                word.append(rus)
                RUS = True
        elif y == 'Sort by word length (English)':
            for leng in leneng(MP3Files):
                word.append(leng)
                RUS = False
        elif y == 'Sort by word length (Russian)':
            for lrus in lenrus(MP3Files):
                word.append(lrus)
                RUS = True
        else:
            for eng in sortingeng(MP3Files):
                word.append(eng)
                RUS = False
        return word, RUS

    def WordTie(self, btn, Option, Num, *args):
        if Num < len(MP3Files) and Num >= 0:
            word, RUS = self.RusOrEng(Option)
            Path, Eng, Rus, Length = self.GetAttributes(Num, RUS, word)
            self.WordListen(Path, Eng, Rus, Length, Option, Num)
        else:
            self.MainMenu

    def WordListen(self, Path, Eng, Rus, Length, Option, Num, *args):
        self.clear_widgets()
        self.PlayMp3File('btn', Path)
        self.cols = 3
        self.add_widget(Label(text='\n'))
        self.EngLabel = Label(text=Eng)
        self.add_widget(self.EngLabel)
        self.add_widget(Label(text='\n'))
        self.add_widget(Label(text='\n'))
        self.add_widget(Label(text=Rus))
        self.add_widget(Label(text='\n'))
        self.btrn1 = Button(text='Previous word')
        self.add_widget(self.btrn1)
        self.btrn1.bind(on_press=lambda btn=None, Option1=Option, Num1=Num - 1: self.WordTie(btn, Option1, Num1))
        self.btrn2 = Button(text='Replay word')
        self.btrn2.bind(on_press=lambda btn=None, Path=Path: self.PlayMp3File(btn, Path))
        self.add_widget(self.btrn2)
        self.btrn3 = Button(text='Next word')
        self.btrn3.bind(on_press=lambda btn=None, Option1=Option, Num1=Num + 1: self.WordTie(btn, Option1, Num1))
        self.add_widget(self.btrn3)
        self.add_widget(Label(text='\n'))
        self.btrn4 = Button(text='Return to menu')
        self.btrn4.bind(on_press=self.MainMenu)
        self.add_widget(self.btrn4)

    def Test(self, *args):
        RandomRus = random.randint(1, 2)
        if RandomRus == 1:
            Option = 'Sort alphabetically (Russian)'
        else:
            Option = 'Sort by word length (English)'
        NOTUSED, RUS = self.RusOrEng(Option)
        word = pickWord()
        RanNum = random.randint(1, len(word))
        for item in MP3Files:
            if word == item.english:
                Path = item.path
                Eng = item.english
                Rus = item.russian
                Length = item.length
        r = pickWord()
        s = pickWord()
        t = pickWord()
        if r or s or t == word:
            r = pickWord()
            s = pickWord()
            t = pickWord()
        for item in MP3Files:
            if r == item.english:
                Pathr = item.path
                Engr = item.english
                Rusr = item.russian
                Lengthr = item.length
        for item in MP3Files:
            if s == item.english:
                Paths = item.path
                Engs = item.english
                Russ = item.russian
                Lengths = item.length
        for item in MP3Files:
            if t == item.english:
                Patht = item.path
                Engt = item.english
                Rust = item.russian
                Lengtht = item.length
        wordlist = []
        if RUS:
            WordDisplayed = Eng
            CorrectWord = Rus
            wordlist.append(Rus)
            wordlist.append(Rusr)
            wordlist.append(Russ)
            wordlist.append(Rust)
        else:
            WordDisplayed = Rus
            CorrectWord = Eng
            wordlist.append(Eng)
            wordlist.append(Engr)
            wordlist.append(Engs)
            wordlist.append(Engt)
        random.shuffle(wordlist)
        self.PlayMp3File('btn', Path)
        self.clear_widgets()
        self.cols = 3
        self.add_widget(Label(text='\n'))
        self.add_widget(Label(text=WordDisplayed))
        self.add_widget(Label(text='\n'))
        self.btrn1 = Button(text=wordlist[0])
        self.btrn1.bind(
            on_press=lambda btn=None, Guess=self.btrn1.text, Actual=CorrectWord: self.Determine(btn, Guess, Actual))
        self.add_widget(self.btrn1)
        self.add_widget(Label(text='\n'))
        self.btrn2 = Button(text=wordlist[1])
        self.btrn2.bind(
            on_press=lambda btn=None, Guess=self.btrn2.text, Actual=CorrectWord: self.Determine(btn, Guess, Actual))
        self.add_widget(self.btrn2)
        self.btrn3 = Button(text=wordlist[2])
        self.btrn3.bind(
            on_press=lambda btn=None, Guess=self.btrn3.text, Actual=CorrectWord: self.Determine(btn, Guess, Actual))
        self.add_widget(self.btrn3)
        self.add_widget(Label(text='\n'))
        self.btrn4 = Button(text=wordlist[3])
        self.btrn4.bind(
            on_press=lambda btn=None, Guess=self.btrn4.text, Actual=CorrectWord: self.Determine(btn, Guess, Actual))
        self.add_widget(self.btrn4)
        self.add_widget(Label(text='\n'))
        self.add_widget(Label(text='\n'))
        self.add_widget(Label(text='\n'))
        self.add_widget(Label(text='\n'))
        self.btrn5 = Button(text='Return to menu')
        self.btrn5.bind(on_press=self.MainMenu)
        self.add_widget(self.btrn5)

    def Determine(self, btn, Guess, Actual, *args):
        if Guess == Actual:
            self.Correct(Guess, Actual)
        else:
            self.Incorrect(Guess, Actual)

    def Correct(self, Guess, Actual, *args):
        updateFileName(Actual, increase=True, reset=False)
        self.clear_widgets()
        self.cols = 1
        self.add_widget(Label(text='Correct!'))
        self.btrn1 = Button(text='Press for next question')
        self.btrn1.bind(on_press=self.Test)
        self.add_widget(self.btrn1)

    def Incorrect(self, Guess, Actual, *args):
        updateFileName(Actual, increase=False, reset=True)
        self.clear_widgets()
        self.cols = 1
        self.add_widget(Label(text='Your answer was incorrect'))
        self.btrn1 = Button(text='Press for next question')
        self.btrn1.bind(on_press=self.Test)
        self.add_widget(self.btrn1)

    def createUser(self, User, Pass, *args):
        '''This creates a new user and their password in the UserPass.csv file and creates a new word box for them, with their username.'''
        c = csv.reader(open("UserPass.csv", "rb"))
        x = False
        for row in c:
            print row[0] + 'Row[0]'
            print User + 'User'
            if row[0] == User:
                print 'Hello'
                x = True
        if x == True:
            self.UserExist()
        elif x == False:
            createWordBoxes(MP3Files, User)
            x = encrypt(Pass)
            p = csv.writer(open("UserPass.csv", "a"))
            p.writerow([User, x])
            self.Menu()

    def readUser(self, User, Pass, *args):
        '''This reads the CSV file and compares the input username/password to
    each username/password in the UserPass.csv file.'''
        c = csv.reader(open("UserPass.csv", "rb"))
        x = False
        global X
        X = User
        for row in c:
            print row
            if row[0] == User and row[1] == encrypt(Pass):
                x = True
                print x
                break
        if x == True:
            global X
            X = User
            print '\n'
            self.MainMenu()
        elif x == False:
            self.WrongPass()

    def WrongPass(self, *args):
        self.clear_widgets()
        self.cols = 1
        self.add_widget(Label(text='Wrong Username Or Password'))
        self.add_widget(Label(text='\n'))
        self.btrn5 = Button(text='Return to menu')
        self.btrn5.bind(on_press=self.Menu)
        self.add_widget(self.btrn5)


class RussianApp(App):
    title = 'Russian Learning Program'

    def build(self):
        return LoginScreen()


class MP3File:
    '''Allows for an instance of this to be made'''

    def __init__(self, path, russian, english, length):
        self.path = path
        self.russian = russian
        self.english = english
        self.length = length


def files():
    '''This creates a list of objects. It can be referenced by files.[attribute]
It gets them from the .xml file'''
    mp3files = []
    for word in root.findall('file'):
        path = word.get('path')
        russian = word.find('word').text
        english = word.find('english').text
        length = word.find('length').text
        mp3files.append(MP3File(path, russian, english, length))
    return mp3files


def sortingeng(files):
    '''This sorts the list of files alphabetically in English'''
    english = []
    x = len(files)
    for i in range(x):
        english.append(files[i].english)
    return sorted(english, key=str.lower)


def lenrus(files):
    '''Sorts the list of files by length of the English word'''
    length = []
    for i in range(len(files)):
        length.append(files[i].russian)
    return sorted(length, key=len)


def leneng(files):
    '''Sorts the list of files by length of the English word'''
    length = []
    for i in range(len(files)):
        length.append(files[i].english)
    return sorted(length, key=len)


def sortingrus(files):
    '''Sorts the list of files alphabetically in Russian'''
    russian = []
    for i in range(len(files)):
        russian.append(files[i].russian)
    sortedruss = sorted(russian, key=unicode.lower)
    rus = []
    for i in sortedruss:
        rus.append(i)
    return rus


def sortreverse(lis):
    '''This reverses a list'''
    p = []
    for i in reversed(lis):
        p.append(i)
    return p


def PlayMp3File(path, eng, item, n=1):
    '''This plays the sound files. The dir may need to be changed'''
    pygame.mixer.init()
    pygame.mixer.music.load(("I:\\0\\" + path))
    pygame.mixer.music.play()
    if n == 1:
        print eng, ':', item
    if n == 2:
        print item, ':', eng
    if n == 3:
        pass
    time.sleep(2)


def createWordBoxes(MP3Files, X):
    '''This creates a csv file that has a list of words, and the number 1
 after each, to indicate its leitner score.'''
    p = csv.writer(open(X + '.csv', "w"))
    for item in MP3Files:
        p.writerow([item.english, 1])


def updateFileName(input_value, increase=False, reset=False):
    '''This updates the input line in the csv file, either resetting it
or increasing it by 1.'''
    try:
        for line in fileinput.input(X + '.csv', inplace=True):
            key, value = line.split(",")
            if key == input_value:
                if increase and int(value) < 5:
                    sys.stdout.write("%s,%s" % (key, int(value) + 1) + '\n')
                elif reset:
                    sys.stdout.write("%s,%s" % (key, 1) + '\n')
                else:
                    sys.stdout.write("%s,%s" % (key, int(value)) + '\n')
                continue
            sys.stdout.write(line)
    finally:
        fileinput.close()


def pickWord():
    '''This places each word in a list by its Leitner number'''
    c = csv.reader(open(X + '.csv', "rb"))
    box1 = []
    box2 = []
    box3 = []
    box4 = []
    box5 = []
    for row in c:
        if row[1] == '1':
            box1.append(row[0])
        elif row[1] == '2':
            box2.append(row[0])
        elif row[1] == '3':
            box3.append(row[0])
        elif row[1] == '4':
            box4.append(row[0])
        elif row[1] == '5':
            box5.append(row[0])
    x = random.randint(0, 100)
    try:
        if x < 50:
            num = random.randint(1, len(box1) - 1)
            word = box1[num]
        if 51 <= x < 80:
            num = random.randint(1, len(box2) - 1)
            word = box2[num]
        if 81 <= x < 90:
            num = random.randint(1, len(box3) - 1)
            word = box3[num]
        if 91 <= x < 97:
            num = random.randint(1, len(box4) - 1)
            word = box4[num]
        if 98 <= x < 100:
            num = random.randint(1, len(box5) - 1)
            word = box5[num]
        return word
    except:
        num = random.randint(1, (len(box1) - 1))
        word = box1[num]
        return word


def Login():
    '''This allows the user to login'''
    print 'Press 1 if you have an account'
    print 'Press 2 if you need to create an account'
    choice = input('Please pick an option: ')
    if choice == 1:
        readUser()
    if choice == 2:
        User, Pass = createUser()
        readUser(User, Pass)
    else:
        print 'That login is wrong'
        Login()


def encrypt(Pass):
    '''This hashes any string inputted'''
    m = hashlib.md5()
    m.update(Pass)
    return m.digest()


def learning(MP3Files, choice=0):
    '''This allows the user to select how to sort the words, and plays each one
in the sorting algorithm that they selected.'''
    while True:
        if choice == 0:
            print '\nYou can sort the files how you like.\n'
            print 'Press 1 to sort them alphabetically in English'
            print 'Press 2 to sort them by word length in English'
            print 'Press 3 to sort them alphabetically in Russian'
            print 'Press 4 to sort them by word length in Russian'
            print 'Press 5 to Return to menu\n'
            choice = input('Please pick an option\n')
        elif choice == 1:
            for eng in sortingeng(MP3Files):
                for item in MP3Files:
                    if eng == item.english:
                        PlayMp3File(item.path, eng, item.russian)
            y = input('\nPress 1 to repeat the words\nPress 2 to return to menu.')
            if y == 1:
                learning(MP3Files, 1)
            else:
                menu(MP3Files)

        elif choice == 2:
            h = input('\nPress 1 to sort in ascending order\nPress 2 to sort in descending order\n')
            if h == 1:
                for leng in leneng(MP3Files):
                    for item in MP3Files:
                        if leng == item.english:
                            PlayMp3File(item.path, leng, item.russian)
            if h == 2:
                for leng in sortreverse(leneng(MP3Files)):
                    for item in MP3Files:
                        if leng == item.english:
                            PlayMp3File(item.path, leng, item.russian)
            y = input('\nPress 1 to repeat the words\nPress 2 to return to menu.')
            if y == 1:
                learning(MP3Files, 2)
            else:
                menu(MP3Files)


        elif choice == 3:
            for rus in sortingrus(MP3Files):
                for item in MP3Files:
                    if rus == item.russian:
                        PlayMp3File(item.path, item.english, rus, 2)
            y = input('\nPress 1 to repeat the words\nPress 2 to return to the menu.')
            if y == 1:
                learning(MP3Files, 3)
            else:
                menu(MP3Files)
            choice = 0


        elif choice == 4:
            h = input('\nPress 1 to sort in ascending order\nPress 2 to sort in descending order\n')
            if h == 1:
                for leng in lenrus(MP3Files):
                    for item in MP3Files:
                        if leng == item.russian:
                            PlayMp3File(item.path, item.english, item.russian, 2)
            if h == 2:
                for leng in sortreverse(lenrus(MP3Files)):
                    for item in MP3Files:
                        if leng == item.russian:
                            PlayMp3File(item.path, item.english, item.russian, 2)
            y = input('\nPress 1 to repeat the words\nPress 2 to reutn to the menu.')
            if y == 1:
                learning(MP3Files, 4)
            else:
                menu(MP3Files)

        else:
            menu(MP3Files)


def menu(MP3Files, y=0):
    '''This is the test function, this allows them to choose how many questions they
want, and allows for input and comparison to the real answer.'''
    if y == 0:
        print "Time for the test!"
        print "Press 1 for 10 questions."
        print "Press 2 for 20 questions"
        print "Press 3 for 30 questions"
        print "Press 9 to return to menu.\n"
        numb = input('Please pick an option.')
        y = 5
    p = len(MP3Files) - 1
    if y == 5:
        for cur in range(numb * 10):
            word = pickWord()
            for item in MP3Files:
                if item.english == word:
                    ENG = word
            x = False
            m = 1
            while x == False:
                if MP3Files[m].english == word:
                    x = True
                    number = m
                else:
                    m = m + 1
            l = rand(3)
            if l == 1:
                print MP3Files[number].english
                k = 'russian'
                r = random.randint(1, p)
                s = random.randint(1, p)
                t = random.randint(1, p)
                if r or s or t == number:
                    r = random.randint(1, p)
                    s = random.randint(1, p)
                    t = random.randint(1, p)
                print MP3Files[number].english
                print MP3Files[r].english
                print MP3Files[s].english
                print MP3Files[t].english
                i = raw_input('What do you think the word was, in ' + k + '?')
                if i == MP3Files[number].english:
                    updateFileName(i, increase=True)
                    print 'Correct!'
                else:
                    updateFileName(i, reset=True)
                    print 'Incorrect.'
            if l == 2:
                print MP3Files[number].russian
                k = 'english'
                r = random.randint(1, p)
                s = random.randint(1, p)
                t = random.randint(1, p)
                if r or s or t == number:
                    r = random.randint(1, p)
                    s = random.randint(1, p)
                    t = random.randint(1, p)
                print MP3Files[number].russian
                print MP3Files[r].russian
                print MP3Files[s].russian
                print MP3Files[t].russian
                i = raw_input('What do you think the word was, in ' + k + '?')
                if i == MP3Files[number].english:
                    updateFileName(i, increase=True)
                    print 'Correct!'
                else:
                    updateFileName(i, reset=True)
                    print 'Incorrect.'
            if l == 3:
                PlayMp3File(MP3Files[number].path, MP3Files[number].english, MP3Files[number].russian, n=3)
                k = 'english(SOUND)'
                r = random.randint(1, p)
                s = random.randint(1, p)
                t = random.randint(1, p)
                if r or s or t == number:
                    r = random.randint(1, p)
                    s = random.randint(1, p)
                    t = random.randint(1, p)
                print MP3Files[number].english
                print MP3Files[r].english
                print MP3Files[s].english
                print MP3Files[t].english
                i = raw_input('What do you think the word was, in ' + k + '?')
                if i == MP3Files[number].english:
                    updateFileName(i, increase=True)
                    print 'Correct!'
                else:
                    updateFileName(i, reset=True)
                    print 'Incorrect.'
        print "\nPress 1 to redo the test"
        print "Press 2 to go back to the test menu"
        print "Press 3 to go back to the main menu"
        o = input("Pick an option please: ")
        if o == 1:
            menu(MP3Files, y=5)
        elif o == 2:
            menu(MP3Files)
        else:
            menu(MP3Files)
    else:
        menu(MP3Files)


def rand(q):
    '''This picks a random number between 1 and the number given.'''
    ran = random.randint(1, q)
    return ran


tree = ET.parse('I:\\index_0 only.xml')  # This will need to be changed to the file path of the xml file
root = tree.getroot()
MP3Files = files()

if __name__ in ('__main__', '__android__'):
    RussianApp().run()
