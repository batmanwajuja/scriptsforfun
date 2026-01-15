' Text-to-Speech VBScript with File and Command-Line Input
Option Explicit

Dim speech, voices
Dim i, voiceIndex
Dim inputText, inputFile
Dim args

Set speech = CreateObject("SAPI.SpVoice")
Set voices = speech.GetVoices
Set args = WScript.Arguments

' -------------------------
' Voice selection
' -------------------------
voiceIndex = 0 ' default voice

If args.Count >= 2 Then
    If IsNumeric(args(args.Count - 1)) Then
        voiceIndex = CInt(args(args.Count - 1))
    End If
End If

If voiceIndex >= 0 And voiceIndex < voices.Count Then
    Set speech.Voice = voices.Item(voiceIndex)
End If

' -------------------------
' Input handling
' -------------------------
inputText = ""

If args.Count > 0 Then

    ' File input mode
    If args(0) = "-f" And args.Count >= 2 Then
        inputFile = args(1)
        inputText = ReadFile(inputFile)

    ' Direct text input
    Else
        inputText = args(0)
    End If

Else
    ' Interactive fallback
    inputText = InputBox("Enter text to speak:", "Text to Speech")
End If

' -------------------------
' Speak
' -------------------------
If Len(inputText) > 0 Then
    speech.Speak inputText
Else
    WScript.Echo "No text provided."
End If


' =========================
' File reading function
' =========================
Function ReadFile(path)
    Dim fso, file, text
    Set fso = CreateObject("Scripting.FileSystemObject")

    If Not fso.FileExists(path) Then
        WScript.Echo "File not found: " & path
        WScript.Quit 1
    End If

    Set file = fso.OpenTextFile(path, 1)
    text = file.ReadAll
    file.Close

    ReadFile = text
End Function
