#!/usr/bin/python


# ----- Imported Modules
import wx
import math
import operator
import string
# ---- Global Functions 

def getResChoices(filename):
	filename = filename + '.txt'
	with open(filename) as f:
		avalRes = []
		avalRes = f.readlines()
	avalRes = [Resistor.strip() for Resistor in avalRes]
	avalRes = [Resistor.upper() for Resistor in avalRes]
	avalRes.sort()
	return avalRes
	
def AddLinearSpacer(boxsizer, pixelSpacing):
	# A one-dimensional spacer for use with any BoxSizer
	orientation = boxsizer.GetOrientation()
	if (orientation == wx.HORIZONTAL):
		boxsizer.Add( (pixelSpacing, 0))
		
	elif (orientation == wx.VERTICAL) :
		boxsizer.Add( (0,pixelSpacing))

def convert (Value):
	# Converts User input string to floating point number
	# So calculations can be done on the inputs
	Value = Value.upper()
	if 'K' in Value:
		Value = string.strip(Value,'K')
		Value = float(Value) * math.pow(10,3)
	elif 'M' in Value:
		Value = string.strip(Value,'M')
		Value = float(Value) * math.pow(10,6)
	else:
		Value = float(Value)
	return Value		

# ----- Classes
class ComboCls:
	def __init__(self,R1,R2,Crnt,RtSd,diff):
		self.R1=R1		# Resistor 1
		self.R2=R2		# Resistor 2, Voltage Droped Across
		self.Crnt=Crnt		# Current Drawn By Resistors
		self.RtSd=RtSd		# Right Side of Voltage Divider Equation
		self.diff=diff		# Difference Between Output Voltage and User Defined
						# Output Voltage
		
class chkbxPanel(wx.Panel):
	# This class defines the Panel that will
	# hold the checkbox containing all of the 
	# resistors
	def __init__(self,parent):
		wx.Panel.__init__(self,parent=parent,id=-1)
		# Widgets
		GroupResList = ['All','E12','Magnum','None']
		self.GroupNo = len(GroupResList)
		StandardResList = getResChoices('aval')
		ResList = GroupResList+StandardResList
		self.noRes = len(ResList)
		Prompt = 'Please Choose Your Resistors'
		self.ResChkBx = wx.CheckListBox(self,id=-1,choices=ResList,size=(-1,500))
		self.PromptChkBx = wx.StaticText(self,id=-1,label=Prompt)
		# Single Page level sizer to position all controls
		# and controls classes' instantiations
		self.panel_vertSizer=wx.BoxSizer(wx.VERTICAL)
		self.panel_vertSizer.Add(self.PromptChkBx,proportion = 0,flag=wx.ALIGN_LEFT)
		AddLinearSpacer(self.panel_vertSizer,2)
		self.panel_vertSizer.Add(self.ResChkBx,proportion=0,flag=wx.ALIGN_LEFT)
		# Invoke the sizer
		self.SetSizer(self.panel_vertSizer)
		# Make "self" (the panel) shrink to the minimum size
		# required by the controls
		self.Fit()
		# end __init__
		
	# -----
		

class userinputPanel(wx.Panel):
	# This class defines the Panel that will
	# contain the user input fields
	def __init__(self, parent):
		wx.Panel.__init__(self,parent=parent,id=-1)
		# Widgets
		uInputVPromptString= 'Please Enter the Input Voltage:'
		uOutputVPromptString= 'Please Enter the Desired Output Voltage:'
		self.uInputVPromptText= wx.StaticText(self,id=-1,label=uInputVPromptString)
		self.uOutputVPromptText= wx.StaticText(self,id=-1,label=uOutputVPromptString)
		self.uInputV= wx.TextCtrl(self, id=-1,style=wx.TE_PROCESS_ENTER)
		self.uOutputV=wx.TextCtrl(self, id=-1,style=wx.TE_PROCESS_ENTER)
		# Single Page level sizer to position all controls
		# and controls classes' instantiations
		self.panel_vertSizer=wx.BoxSizer(wx.VERTICAL)
		self.panel_vertSizer.Add(self.uInputVPromptText,proportion=0,flag=wx.ALIGN_LEFT)
		AddLinearSpacer(self.panel_vertSizer,2)
		self.panel_vertSizer.Add(self.uInputV,proportion=0,flag=wx.ALIGN_LEFT)
		AddLinearSpacer(self.panel_vertSizer,5)
		self.panel_vertSizer.Add(self.uOutputVPromptText,proportion=0,flag=wx.ALIGN_LEFT)
		AddLinearSpacer(self.panel_vertSizer,2)
		self.panel_vertSizer.Add(self.uOutputV,proportion=0, flag=wx.ALIGN_LEFT) 
		# Invoke the sizer
		self.SetSizer(self.panel_vertSizer)
		# Make "self" (the panel) shrink to the minimum size
		# required by the controls
		self.Fit()	
		# end __init__
		
class ResultsPanel (wx.Panel):
	# This class defines the Panel that will
	# show the results of the calculations
	def __init__(self, parent):
		wx.Panel.__init__(self,parent=parent,id=-1)
		# Widgets
		ResultsPanelTitle = 'Results:'
		self.ResultsText = wx.StaticText(self, id=-1, label=ResultsPanelTitle)
		self.Results = wx.TextCtrl(self, id=-1,size=(300,500),style=(wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_DONTWRAP))
		
		# Single Page level Sizer to position all controls
		# and controls classes' instantiations
		self.panel_vertSizer=wx.BoxSizer(wx.VERTICAL)
		self.panel_vertSizer.Add(self.ResultsText,proportion=0, flag=wx.ALIGN_CENTRE)
		AddLinearSpacer(self.panel_vertSizer,10)
		self.panel_vertSizer.Add(self.Results, proportion=0,flag=wx.ALL)
		
		# Invoke the sizer
		self.SetSizer(self.panel_vertSizer)
		# Make "self" (the panel) shrink to the minimum size
		# required by the controls
		self.Fit()	
		
		# end __init__
		
		
# ----- Main Frame
class MainFrame(wx.Frame):
	# A 3-Control class with BoxSizers
	def __init__(self):
		# Configure the Frame 
		titleText='Resistor Divider Calculator'
		wx.Frame.__init__(	self,None,title=titleText
						,size=(600,300),style=wx.DEFAULT_FRAME_STYLE)
		self.Position =(100,0)
		# First Frame Control automatically expands to the 
		# Frame's client size.
		frame_panel = wx.Panel(self)
		
		# Create the Controls
		self.LeftPanel = chkbxPanel(frame_panel)
		self.MiddlePanel = userinputPanel(frame_panel)
		self.RightPanel = ResultsPanel(frame_panel)
		
		# Create Sizers and add the controls 
		panelCtrls_horzSizer = wx.BoxSizer(wx.HORIZONTAL)
		
		AddLinearSpacer(panelCtrls_horzSizer, 35)
		panelCtrls_horzSizer.Add(self.LeftPanel)
		AddLinearSpacer(panelCtrls_horzSizer, 35)
		panelCtrls_horzSizer.Add(self.MiddlePanel)
		AddLinearSpacer(panelCtrls_horzSizer, 35)
		panelCtrls_horzSizer.Add(self.RightPanel)
		AddLinearSpacer(panelCtrls_horzSizer, 35)
		
		framePanel_vertSizer = wx.BoxSizer(wx.VERTICAL)
		
		AddLinearSpacer(framePanel_vertSizer,35)
		framePanel_vertSizer.Add(panelCtrls_horzSizer)
		AddLinearSpacer(framePanel_vertSizer,35)
		
		frame_panel.SetSizer(framePanel_vertSizer)
		frame_panel.Fit()
		self.SetSize((900,600))
		
		# Bind Events
		self.LeftPanel.ResChkBx.Bind(wx.EVT_CHECKLISTBOX,self.onCheckBox)
		self.MiddlePanel.uInputV.Bind(wx.EVT_TEXT_ENTER,self.onInputV)
		self.MiddlePanel.uOutputV.Bind(wx.EVT_TEXT_ENTER,self.onOutputV)
		
	# Event Handler Functions
	def onCheckBox(self, event):
		checked = event.EventObject.CheckedStrings
		#self.RightPanel.Results.AppendText('Qty checked:{0}\n'.format(len(checked)))
		all_list = range(self.LeftPanel.GroupNo,self.LeftPanel.noRes)
		#print 'Number of Resistors: {0}'.format(self.LeftPanel.noRes)
		if self.LeftPanel.ResChkBx.IsChecked(0):
			self.LeftPanel.ResChkBx.SetChecked(all_list)
		if self.LeftPanel.ResChkBx.IsChecked(1):
			E12Res=[]
			E12Res=getResChoices('E12')
			self.LeftPanel.ResChkBx.SetCheckedStrings(E12Res)
		if self.LeftPanel.ResChkBx.IsChecked(2):
			MagRes=[]
			MagRes=getResChoices('Magnum')
			self.LeftPanel.ResChkBx.SetCheckedStrings(MagRes)
		if self.LeftPanel.ResChkBx.IsChecked(3):
			NoneChoice=[]
			self.LeftPanel.ResChkBx.SetCheckedStrings(NoneChoice)
	
	
	def onInputV(self, event): 
		#print 'Input Event'
		self.Input = event.EventObject.Value
	def onOutputV(self,event):
		#print 'Ouput Event'
		self.Output = event.EventObject.Value
		self.ResCalcLogic(self.Input,self.Output)
	
	# Logic Functions
	def ResCalcLogic(self,InputV,OutputV):
		#print 'Logic Function'
		#print InputV
		#print OutputV
		perc=0.01
		Input=float(InputV)
		Output=float(OutputV)
		CalOutV = perc * float(OutputV)
		self.Combos=[]
		# Create List of Resistors used
		self.Resistors=[]
		self.Resistors=list(self.LeftPanel.ResChkBx.GetCheckedStrings())
		for indx, Resistor in enumerate(self.Resistors):
			self.Resistors[indx] = convert(Resistor)
		# print self.Resistors
		# Calculate Voltage Divider
		while True:
			for Res1 in self.Resistors:
				CalOutV = perc * float(OutputV)
				for Res2 in self.Resistors:
					# Right Side of equation
					RS = (Input*(Res2/(Res1+Res2)))
					if (RS>=(Output-CalOutV)) and (RS<=(Output+CalOutV)):
						Current = Input / (Res1+Res2)
						diff = Output - RS
						self.Combos.append(ComboCls(Res1,Res2,Current,RS,diff))		
			if len(self.Combos)>=10:
				break
			else:
				perc+=0.01
		
		self.Combos.sort(key = operator.attrgetter('diff'))
		i=1
		show = 21
		self.RightPanel.Results.AppendText('Sorted By Output Voltage\n')
		self.RightPanel.Results.AppendText('With in {0}% of {1}V\n'.format((perc*100),OutputV))
		for combo in self.Combos:
			self.RightPanel.Results.AppendText('---------- Combination {0} ----------\n'.format(i))
			self.RightPanel.Results.AppendText('Resistor 1: {0}\n'.format(self.Combos[i].R1))
			self.RightPanel.Results.AppendText('Resistor 2: {0}\n'.format(self.Combos[i].R2))
			self.RightPanel.Results.AppendText('Calculated Output Voltage: {0:0.4}\n'.format(self.Combos[i].RtSd))
			i+=1
			if i>= show:
				break
				
		
# ----- Main if statement
if __name__ == '__main__':
	app = wx.PySimpleApp(redirect=True)
	appFrame = MainFrame().Show()
	app.MainLoop()
	
	
	
	
	
