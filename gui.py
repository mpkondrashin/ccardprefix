from Tkinter import *
import tkFileDialog
import ccardprefix

def LoadPrefixes(ev):
    fn = tkFileDialog.Open(root, filetypes = [('*.txt files', '.txt')]).show()
    if fn == '':
        return
    prefixesTextbox.config(state=NORMAL)
    prefixesTextbox.delete('1.0', 'end') 
    prefixesTextbox.insert('1.0', open(fn, 'rt').read())
    prefixesTextbox.config(state=DISABLED)

def LoadTemplate(ev):
    fn = tkFileDialog.Open(root, filetypes = [('*.xml files', '.xml')]).show()
    if fn == '':
        return
    templateTextbox.config(state=NORMAL)
    templateTextbox.delete('1.0', 'end') 
    templateTextbox.insert('1.0', open(fn, 'rt').read())
    templateTextbox.config(state=DISABLED)

def Generate(ev):
    prefixes = prefixesTextbox.get("1.0",END)
    template = templateTextbox.get("1.0",END)
    result = ccardprefix.generate_template(prefixes, template)
    generateTextbox.delete('1.0', 'end') 
    generateTextbox.insert('1.0', result)
    
def SaveFile(ev):
    fn = tkFileDialog.SaveAs(root, filetypes = [('*.xml files', '.xml')]).show()
    if fn == '':
        return
    if not fn.endswith(".xml"):
        fn+=".xml"
    open(fn, 'wt').write(generateTextbox.get('1.0', 'end'))

def Help(ev):
    t = Toplevel(root)
    t.wm_title("Help")
    #l = Label(t, text="This is window #%s" % 1)
    text = Text(t, font='Arial 14', wrap='word')
    text.insert('1.0', """
        This program can be used to generate DLP templates for Trend Micro products
        
1. Load prefixes file
2. Load template file
3. Press generate Button
4. Save resulting template to file
5. Import template file using console of Trend Micro product

See more detail on prefixes file and template file in README.txt
""")
    text.config(state=DISABLED)
    text.pack()#side="top", fill="both", expand=True, padx=100, pady=100)
    

def Quit(ev):
    global root
    root.destroy()


root = Tk()
root.wm_title("Credit Card DLP Template Generator")

prefixLabelFrame = LabelFrame(root, text="1.")#, padx=5, pady=5)
prefixLabelFrame.grid(row=0, column=0)#, padx=10, pady=10)

loadPrefixesBtn = Button(prefixLabelFrame, text = 'Load Prefixes')
loadPrefixesBtn.bind("<Button-1>", LoadPrefixes)
loadPrefixesBtn.grid(row=0, column=0)

prefixFrame = Frame(root, height = 60, bg = 'gray')
textFrame = Frame(root, height = 340, width = 600)

prefixesTextbox = Text(prefixLabelFrame, font='Arial 14', width=10)#, wrap='word')
prefixesTextbox.grid(row=1, column=0)#side = 'left', fill = 'both', expand = 1)

templateLabelFrame = LabelFrame(root, text="2.")#, padx=5, pady=5)
templateLabelFrame.grid(row=0, column=1)#, padx=10, pady=10)

loadTemplateBtn = Button(templateLabelFrame, text = 'Load Template')
loadTemplateBtn.bind("<Button-1>", LoadTemplate)
loadTemplateBtn.grid(row=0, column=0)

templateTextbox = Text(templateLabelFrame, font='Arial 14', wrap="none", width=40)
templateTextbox.grid(row=1, column=0)#side = 'left', fill = 'both', expand = 1)


templateLabelFrame = LabelFrame(root, text="3.")#, padx=5, pady=5)
templateLabelFrame.grid(row=0, column=2)#, padx=10, pady=10)

generateBtn = Button(templateLabelFrame, text = 'Generate')
generateBtn.bind("<Button-1>", Generate)
generateBtn.grid(row=0, column=0)

saveBtn = Button(templateLabelFrame, text = 'Save')
saveBtn.bind("<Button-1>", SaveFile)
saveBtn.grid(row=0, column=1)

helpBtn = Button(root, text = 'Help')
helpBtn.bind("<Button-1>", Help)
helpBtn.grid(row=1, column=0)


quitBtn = Button(root, text = 'Quit')
quitBtn.bind("<Button-1>", Quit)
quitBtn.grid(row=1, column=2)

generateTextbox = Text(templateLabelFrame, font='Arial 14', wrap="none", width=40)
generateTextbox.grid(row=1, column=0, columnspan=3)#side = 'left', fill = 'both', expand = 1)


#loadPrefixesBtn.place(x = 10, y = 10, width = 40, height = 40)
'''

templLabelFrame = LabelFrame(root, text="Template", padx=5, pady=5)
templLabelFrame.pack(padx=10, pady=10)

loadTemplateBtn = Button(prefixLabelFrame, text = 'Load Template')
loadTemplateBtn.bind("<Button-1>", LoadPrefixes)
loadTemplateBtn.place(x = 10, y = 10, width = 40, height = 40)


panelFrame = Frame(root, height = 60, bg = 'gray')
textFrame = Frame(root, height = 340, width = 600)

panelFrame.pack(side = 'top', fill = 'x')
textFrame.pack(side = 'bottom', fill = 'both', expand = 1)

#textFrame2 = Frame(root, height = 340, width = 300)
#textFrame2.pack(side = 'bottom', fill = 'both', expand = 1)

prefixesTextbox = Text(textFrame, font='Arial 14', wrap='word')

prefixesTextbox.pack(side = 'left', fill = 'both', expand = 1)
scrollbar.pack(side = 'right', fill = 'y')

loadBtn = Button(panelFrame, text = 'Load')
saveBtn = Button(panelFrame, text = 'Save')
genBtn = Button(panelFrame, text = 'Generate')
quitBtn = Button(panelFrame, text = 'Quit')

loadBtn.bind("<Button-1>", LoadFile)
saveBtn.bind("<Button-1>", SaveFile)
genBtn.bind("<Button-1>", Generate)
quitBtn.bind("<Button-1>", Quit)

loadBtn.place(x = 10, y = 10, width = 40, height = 40)
saveBtn.place(x = 60, y = 10, width = 40, height = 40)
genBtn.place(x = 110, y = 10, width = 40, height = 40)
quitBtn.place(x = 160, y = 10, width = 40, height = 40)
'''
root.mainloop()