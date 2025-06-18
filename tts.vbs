' Text-to-Speech VBScript with Voice Selection

Option Explicit

Dim speech, voices, voiceList, voiceIndex, i, selectedVoice
Dim userText, voiceName

' Create a SAPI.SpVoice object
Set speech = CreateObject("SAPI.SpVoice")

' Get list of available voices
Set voices = speech.GetVoices
voiceList = ""

' Build a numbered list of voice names
For i = 0 To voices.Count - 1
    voiceList = voiceList & i & ": " & voices.Item(i).GetDescription & vbCrLf
Next

' Ask the user to pick a voice
voiceIndex = InputBox("Available Voices:" & vbCrLf & voiceList & vbCrLf & "Enter the number of the voice you want to use:", "Choose Voice", "0")

' Validate the voice index
If IsNumeric(voiceIndex) Then
    voiceIndex = CInt(voiceIndex)
    If voiceIndex >= 0 And voiceIndex < voices.Count Then
        Set speech.Voice = voices.Item(voiceIndex)
        voiceName = speech.Voice.GetDescription
    Else
        MsgBox "Invalid voice index. Default voice will be used."
    End If
Else
    MsgBox "Invalid input. Default voice will be used."
End If

' Ask for text input
userText = InputBox("Enter the text you want to be spoken:", "Text to Speech")

' Speak the text
If Len(userText) > 0 Then
    speech.Speak userText
Else
    MsgBox "No text entered."
End If
