#!/usr/bin/env python3
import os

ut_ini_content = """
[URL]
Protocol=unreal
ProtocolDescription=Unreal Protocol
Name=Player
Map=Index.unr
LocalMap=CityIntro.unr
Host=
Portal=
MapExt=unr
SaveExt=usa
Port=7777
Class=Botpack.TMale1

[FirstRun]
FirstRun=436

[PackageRemap]
UnrealShare=UnrealI

[Engine.Engine]
GameRenderDevice=SDLSoftDrv.SDLSoftwareRenderDevice
WindowedRenderDevice=SDLSoftDrv.SDLSoftwareRenderDevice
RenderDevice=SDLSoftDrv.SDLSoftwareRenderDevice
AudioDevice=ALAudio.ALAudioSubsystem
NetworkDevice=IpDrv.TcpNetDriver
DemoRecordingDevice=Engine.DemoRecDriver
Console=UTMenu.UTConsole
Language=int
GameEngine=Engine.GameEngine
EditorEngine=Editor.EditorEngine
DefaultGame=Botpack.DeathMatchPlus
DefaultServerGame=Botpack.DeathMatchPlus
ViewportManager=SDLDrv.SDLClient
Render=Render.Render
Input=Engine.Input
Canvas=Engine.Canvas

[Core.System]
PurgeCacheDays=30
SavePath=..\Save
CachePath=..\Cache
CacheExt=.uxx
Paths=..\System\*.u
Paths=..\Maps\*.unr
Paths=..\Textures\*.utx
Paths=..\Sounds\*.uax
Paths=..\Music\*.umx
Suppress=DevLoad
Suppress=DevSave
Suppress=DevNetTraffic
Suppress=DevGarbage
Suppress=DevKill
Suppress=DevReplace
Suppress=DevSound
Suppress=DevCompile
Suppress=DevBind
Suppress=DevBsp

[Engine.GameEngine]
CacheSizeMegs=64
UseSound=True
ServerActors=IpDrv.UdpBeacon
ServerActors=IpServer.UdpServerQuery
ServerActors=IpServer.UdpServerUplink MasterServerAddress=unreal.epicgames.com MasterServerPort=27900
ServerActors=IpServer.UdpServerUplink MasterServerAddress=master0.gamespy.com MasterServerPort=27900
ServerActors=IpServer.UdpServerUplink MasterServerAddress=master.mplayer.com MasterServerPort=27900
ServerActors=UWeb.WebServer
ServerPackages=SoldierSkins
ServerPackages=CommandoSkins
ServerPackages=FCommandoSkins
ServerPackages=SGirlSkins
ServerPackages=BossSkins
ServerPackages=Botpack

[SDLDrv.SDLClient]
WindowedViewportX=640
WindowedViewportY=480
WindowedColorBits=16
FullscreenViewportX=1920
FullscreenViewportY=1080
FullscreenColorBits=16
Brightness=0.500000
MipFactor=1.000000
SlowVideoBuffering=False
StartupFullscreen=True
CurvedSurfaces=False
CaptureMouse=False
LowDetailTextures=False
ScreenFlashes=True
NoLighting=False
DeadZoneX=True
DeadZoneY=True
DeadZoneZ=False
DeadZoneR=False
DeadZoneU=False
DeadZoneV=False
InvertVertical=False
ScaleX=1000.000000
ScaleY=1000.000000
ScaleZ=1000.000000
ScaleR=300.000000
ScaleU=1000.000000
ScaleV=1000.000000
ScaleJBX=0.025000
ScaleJBY=0.025000
MinDesiredFrameRate=0.000000
NoDynamicLights=False
Decals=True
NoFractalAnim=False
SkinDetail=High
TextureDetail=High
ParticleDensity=0
UseJoystick=False
JoystickNumber=0

[SDLGLDrv.SDLGLRenderDevice]
UseTNT=1
UseGammaExtension=0
UseModulatedGamma=0
UseS3TC=0
OpenGLLibName=libGL.so.1
MinDepthBits=16
MaxLogUOverV=8
MaxLogVOverU=8
UseMultiTexture=1
UsePalette=1
UseAlphaPalette=0
ShareLists=0
AlwaysMipmap=0
DoPrecache=0
Translucency=True
VolumetricLighting=True
ShinySurfaces=True
Coronas=True
HighDetailActors=True
DetailTextures=True
UseTrilinear=False

[OpenGLDrv.OpenGLRenderDevice]
UseTNT=1
UseGammaExtension=1
UseModulatedGamma=0
UseS3TC=0
OpenGLLibName=libGL.so.1
MinDepthBits=16
MaxLogUOverV=8
MaxLogVOverU=8
UseMultiTexture=1
UsePalette=1
UseAlphaPalette=0
ShareLists=0
AlwaysMipmap=0
DoPrecache=0
Translucency=True
VolumetricLighting=True
ShinySurfaces=True
Coronas=True
HighDetailActors=True
DetailTextures=True
UseTrilinear=False

[SDLSoftDrv.SDLSoftwareRenderDevice]
Translucency=True
VolumetricLighting=True
ShinySurfaces=False
Coronas=False
HighDetailActors=False
HighResTextureSmooth=True
LowResTextureSmooth=False
FastTranslucency=True

[Engine.Player]
ConfiguredInternetSpeed=20000
ConfiguredLanSpeed=20000

[Audio.GenericAudioSubsystem]
UseFilter=True
UseSurround=False
UseStereo=True
UseCDMusic=False
UseDigitalMusic=True
UseSpatial=False
UseReverb=False
Use3dHardware=False
LowSoundQuality=False
ReverseStereo=False
Latency=40
OutputRate=22050Hz
Channels=16
MusicVolume=192
SoundVolume=192
AmbientFactor=0.700000
DopplerSpeed=0.000000

[ALAudio.ALAudioSubsystem]
UseFilter=True
UseSurround=False
UseStereo=True
UseCDMusic=False
UseDigitalMusic=True
UseSpatial=True
UseReverb=True
Use3dHardware=False
LowSoundQuality=False
ReverseStereo=False
Latency=40
OutputRate=22050Hz
Channels=16
MusicVolume=192
SoundVolume=192
AmbientFactor=0.700000
DopplerSpeed=0.000000
MusicBufferSize=16384

[IpDrv.TcpNetDriver]
AllowDownloads=True
ConnectionTimeout=15.0
InitialConnectTimeout=300.0
AckTimeout=1.0
KeepAliveTime=0.2
MaxClientRate=20000
SimLatency=0
RelevantTimeout=5.0
SpawnPrioritySeconds=1.0
ServerTravelPause=4.0
NetServerMaxTickRate=20
LanServerMaxTickRate=35
DownloadManagers=IpDrv.HTTPDownload
DownloadManagers=Engine.ChannelDownload

[Engine.DemoRecDriver]
DemoSpectatorClass=Botpack.CHSpectator
MaxClientRate=25000
ConnectionTimeout=15.0
InitialConnectTimeout=500.0
AckTimeout=1.0
KeepAliveTime=1.0
SimLatency=0
RelevantTimeout=5.0
SpawnPrioritySeconds=1.0
ServerTravelPause=4.0
NetServerMaxTickRate=60
LanServerMaxTickRate=60

[Engine.GameReplicationInfo]
ServerName=Linux UT Server
ShortName=UT Server
AdminName=
AdminEmail=
Region=0
MOTDLine1=
MOTDLine2=
MOTDLine3=
MOTDLine4=

[IpDrv.TcpipConnection]
SimPacketLoss=0
SimLatency=0

[IpServer.UdpServerUplink]
DoUpLink=False
UpdateMinutes=1
MasterServerPort=27900

[IpServer.UdpServerQuery]
GameName=ut

[IpDrv.UdpBeacon]
DoBeacon=True
BeaconTime=0.50
BeaconTimeout=5.0
BeaconProduct=ut

[GlideDrv.GlideRenderDevice]
Translucency=True
VolumetricLighting=True
ShinySurfaces=True
Coronas=True
HighDetailActors=True
DetailBias=-1.500000
RefreshRate=60Hz
DetailTextures=True
FastUglyRefresh=False
ScreenSmoothing=True
Resolution=Default

[Editor.EditorEngine]
UseSound=True
CacheSizeMegs=6
GridEnabled=True
SnapVertices=True
SnapDistance=10.000000
GridSize=(X=16.000000,Y=16.000000,Z=16.000000)
RotGridEnabled=True
RotGridSize=(Pitch=1024,Yaw=1024,Roll=1024)
GameCommandLine=-log
FovAngleDegrees=90.000000
GodMode=True
AutoSave=False
AutoSaveTimeMinutes=5
AutoSaveIndex=6
C_WorldBox=(R=0,G=0,B=107,A=0)
C_GroundPlane=(R=0,G=0,B=63,A=0)
C_GroundHighlight=(R=0,G=0,B=127,A=0)
C_BrushWire=(R=255,G=63,B=63,A=0)
C_Pivot=(R=0,G=255,B=0,A=0)
C_Select=(R=0,G=0,B=127,A=0)
C_AddWire=(R=127,G=127,B=255,A=0)
C_SubtractWire=(R=255,G=192,B=63,A=0)
C_GreyWire=(R=163,G=163,B=163,A=0)
C_Invalid=(R=163,G=163,B=163,A=0)
C_ActorWire=(R=127,G=63,B=0,A=0)
C_ActorHiWire=(R=255,G=127,B=0,A=0)
C_White=(R=255,G=255,B=255,A=0)
C_SemiSolidWire=(R=127,G=255,B=0,A=0)
C_NonSolidWire=(R=63,G=192,B=32,A=0)
C_WireGridAxis=(R=119,G=119,B=119,A=0)
C_ActorArrow=(R=163,G=0,B=0,A=0)
C_ScaleBox=(R=151,G=67,B=11,A=0)
C_ScaleBoxHi=(R=223,G=149,B=157,A=0)
C_Mover=(R=255,G=0,B=255,A=0)
C_OrthoBackground=(R=163,G=163,B=163,A=0)
C_Current=(R=0,G=0,B=0,A=0)
C_BrushVertex=(R=0,G=0,B=0,A=0)
C_BrushSnap=(R=0,G=0,B=0,A=0)
C_Black=(R=0,G=0,B=0,A=0)
C_Mask=(R=0,G=0,B=0,A=0)
C_WireBackground=(R=0,G=0,B=0,A=0)
C_ZoneWire=(R=0,G=0,B=0,A=0)
EditPackages=Core
EditPackages=Engine
EditPackages=Editor
EditPackages=UWindow
EditPackages=Fire
EditPackages=IpDrv
EditPackages=UWeb
EditPackages=UBrowser
EditPackages=UnrealShare
EditPackages=UnrealI
EditPackages=UMenu
EditPackages=IpServer
EditPackages=Botpack
EditPackages=UTServerAdmin
EditPackages=UTMenu
EditPackages=UTBrowser

[UMenu.UnrealConsole]
RootWindow=UMenu.UMenuRootWindow
UWindowKey=IK_Esc
ShowDesktop=True

[UMenu.UMenuMenuBar]
ShowHelp=True
GameUMenuDefault=UTMenu.UTGameMenu
MultiplayerUMenuDefault=UTMenu.UTMultiplayerMenu
OptionsUMenuDefault=UTMenu.UTOptionsMenu
ModMenuClass=UMenu.UMenuModMenu

[Botpack.ChallengeBotInfo]
Difficulty=1
Difficulty=1

[Botpack.DeathMatchPlus]
bNoviceMode=True
bHardCoreMode=True
bUseTranslocator=False
bCoopWeaponMode=False
MinPlayers=0
AirControl=0.350000
bChangeLevels=True
bMegaSpeed=False
bAltScoring=False
bTournament=False
NetWait=10
RestartWait=15
InitialBots=5
FragLimit=30
TimeLimit=0
bMultiWeaponStay=True
bForceRespawn=False
MaxCommanders=0
bNoMonsters=True
bHumansOnly=False
bClassicDeathMessages=False

[Botpack.CTFGame]
bUseTranslocator=True
bCoopWeaponMode=True
GoalTeamScore=3

[Botpack.Domination]
bDumbDown=True
bUseTranslocator=True
bCoopWeaponMode=True
GoalTeamScore=100

[Botpack.Assault]
bUseTranslocator=False
bCoopWeaponMode=True

[Botpack.TeamGamePlus]
bBalanceTeams=True
GoalTeamScore=30
bPlayersBalanceTeams=True

[Engine.GameInfo]
bLowGore=False
bVeryLowGore=False
bMuteSpectators=False
bNoCheating=True
bAllowFOV=False
AutoAim=0.930000
GameSpeed=1.000000
MaxSpectators=2
AdminPassword=
GamePassword=
MaxPlayers=16
IPPolicies[0]=ACCEPT,*
IPPolicies[1]=
IPPolicies[2]=
IPPolicies[3]=
IPPolicies[4]=
IPPolicies[5]=
IPPolicies[6]=
IPPolicies[7]=
IPPolicies[8]=
IPPolicies[9]=
IPPolicies[10]=
IPPolicies[11]=
IPPolicies[12]=
IPPolicies[13]=
IPPolicies[14]=
IPPolicies[15]=
IPPolicies[16]=
IPPolicies[17]=
IPPolicies[18]=
IPPolicies[19]=
IPPolicies[20]=
IPPolicies[21]=
IPPolicies[22]=
IPPolicies[23]=
IPPolicies[24]=
IPPolicies[25]=
IPPolicies[26]=
IPPolicies[27]=
IPPolicies[28]=
IPPolicies[29]=
IPPolicies[30]=
IPPolicies[31]=
IPPolicies[32]=
IPPolicies[33]=
IPPolicies[34]=
IPPolicies[35]=
IPPolicies[36]=
IPPolicies[37]=
IPPolicies[38]=
IPPolicies[39]=
IPPolicies[40]=
IPPolicies[41]=
IPPolicies[42]=
IPPolicies[43]=
IPPolicies[44]=
IPPolicies[45]=
IPPolicies[46]=
IPPolicies[47]=
IPPolicies[48]=
IPPolicies[49]=
ServerLogName=server.log
bLocalLog=False
bWorldLog=True
bBatchLocal=False
DemoBuild=0
DemoHasTuts=0
bExternalBatcher=False
bNoMonsters=False
bHumansOnly=False
bCoopWeaponMode=False
bClassicDeathMessages=False

[UnrealShare.UnrealGameOptionsMenu]
bCanModifyGore=True

[UBrowser.UBrowserMainClientWindow]
LANTabName=UBrowserLAN
ServerListNames[0]=UBrowserUT
ServerListNames[1]=UBrowserLAN
ServerListNames[2]=UBrowserPopulated
ServerListNames[3]=UBrowserDeathmatch
ServerListNames[4]=UBrowserTeamGames
ServerListNames[5]=UBrowserCTF
ServerListNames[6]=UBrowserDOM
ServerListNames[7]=UBrowserAS
ServerListNames[8]=UBrowserLMS
ServerListNames[9]=UBrowserAll
ServerListNames[10]=None
ServerListNames[11]=None
ServerListNames[12]=None
ServerListNames[13]=None
ServerListNames[14]=None
ServerListNames[15]=None
ServerListNames[16]=None
ServerListNames[17]=None
ServerListNames[18]=None
ServerListNames[19]=None
ServerListNames[20]=None
ServerListNames[21]=None
ServerListNames[22]=None
ServerListNames[23]=None
ServerListNames[24]=None
ServerListNames[25]=None
ServerListNames[26]=None
ServerListNames[27]=None
ServerListNames[28]=None
ServerListNames[29]=None
ServerListNames[30]=None
ServerListNames[31]=None
ServerListNames[32]=None
ServerListNames[33]=None
ServerListNames[34]=None
ServerListNames[35]=None
ServerListNames[36]=None
ServerListNames[37]=None
ServerListNames[38]=None
ServerListNames[39]=None
ServerListNames[40]=None
ServerListNames[41]=None
ServerListNames[42]=None
ServerListNames[43]=None
ServerListNames[44]=None
ServerListNames[45]=None
ServerListNames[46]=None
ServerListNames[47]=None
ServerListNames[48]=None
ServerListNames[49]=None
bKeepMasterServer=False

[UBrowserUT]
ListFactories[0]=UBrowser.UBrowserSubsetFact,SupersetTag=UBrowserAll,bCompatibleServersOnly=True

[UBrowserLAN]
ListFactories[0]=UBrowser.UBrowserLocalFact,BeaconProduct=ut
URLAppend=?LAN
AutoRefreshTime=10
bNoAutoSort=True

[UBrowserPopulated]
ListFactories[0]=UBrowser.UBrowserSubsetFact,SupersetTag=UBrowserAll,MinPlayers=1,bCompatibleServersOnly=True

[UBrowserDeathmatch]
ListFactories[0]=UBrowser.UBrowserSubsetFact,SupersetTag=UBrowserAll,GameType=DeathMatchPlus,bCompatibleServersOnly=True

[UBrowserTeamGames]
ListFactories[0]=UBrowser.UBrowserSubsetFact,SupersetTag=UBrowserAll,GameType=TeamGamePlus,bCompatibleServersOnly=True

[UBrowserCTF]
ListFactories[0]=UBrowser.UBrowserSubsetFact,SupersetTag=UBrowserAll,GameType=CTFGame,bCompatibleServersOnly=True

[UBrowserDOM]
ListFactories[0]=UBrowser.UBrowserSubsetFact,SupersetTag=UBrowserAll,GameType=Domination,bCompatibleServersOnly=True

[UBrowserAS]
ListFactories[0]=UBrowser.UBrowserSubsetFact,SupersetTag=UBrowserAll,GameType=Assault,bCompatibleServersOnly=True

[UBrowserLMS]
ListFactories[0]=UBrowser.UBrowserSubsetFact,SupersetTag=UBrowserAll,GameType=LastManStanding,bCompatibleServersOnly=True

[UBrowserAll]
ListFactories[0]=UBrowser.UBrowserGSpyFact,MasterServerAddress=unreal.epicgames.com,MasterServerTCPPort=28900,Region=0,GameName=ut
ListFactories[1]=UBrowser.UBrowserGSpyFact,MasterServerAddress=master0.gamespy.com,MasterServerTCPPort=28900,Region=0,GameName=ut
bHidden=True
bFallbackFactories=True

[UTMenu.UTMultiplayerMenu]

[UWeb.WebServer]
Applications[0]=UTServerAdmin.UTServerAdmin
ApplicationPaths[0]=/ServerAdmin
Applications[1]=UTServerAdmin.UTImageServer
ApplicationPaths[1]=/images
DefaultApplication=0
bEnabled=False
ListenPort=5080
MaxConnections=30

[UTServerAdmin.UTServerAdmin]
AdminUsername=lxadmin
AdminPassword=lxadmin

[IpDrv.HTTPDownLoad]
RedirectToURL=
ProxyServerHost=
ProxyServerPort=3128
UseCompression=True

[Engine.StatLog]
LocalBatcherURL=../NetGamesUSA.com/ngStats/ngStatsUT
LocalBatcherParams=
LocalStatsURL=../NetGamesUSA.com/ngStats/html/ngStats_Main.html
WorldBatcherURL=../NetGamesUSA.com/ngWorldStats/bin/ngWorldStats
WorldBatcherParams=-d ../NetGamesUSA.com/ngWorldStats/logs -g UT
WorldStatsURL=http://www.netgamesusa.com
LocalLogDir=../Logs
WorldLogDir=../NetGamesUSA.com/ngWorldStats/logs
bWorldBatcherError=False

[Botpack.UTIntro]
CityIntroHUDClass=
bNoMonsters=False
bHumansOnly=False
bCoopWeaponMode=False
bClassicDeathMessages=False

[UMenu.UMenuRootWindow]
GUIScale=1.000000
LookAndFeelClass=UMenu.UMenuBlueLookAndFeel

[UTMenu.UTConsole]
SpeechKey=86
SavedPasswords[0]=
SavedPasswords[1]=
SavedPasswords[2]=
SavedPasswords[3]=
SavedPasswords[4]=
SavedPasswords[5]=
SavedPasswords[6]=
SavedPasswords[7]=
SavedPasswords[8]=
SavedPasswords[9]=
RootWindow=UMenu.UMenuRootWindow
MouseScale=1.700000
ShowDesktop=True
bShowConsole=False
UWindowKey=IK_None

[UWindow.WindowConsole]
ConsoleKey=192

[RocketArena.RocketArenaGame]
NewVoiceThemeName=RocketArena.RAVoiceMale
HUDTeamDisplay=1
Force1on1=False
ForceInstantRocketFire=False
DisallowSpectatorSpeech=False
BouncyHeight=2.250000
FallingDamage=False
PreferredPickupClass=Class'RocketArena.ArenaGame_Clan'
FragLimit=0
TimeLimit=20
bMultiWeaponStay=True
bForceRespawn=False
bUseTranslocator=False
MaxCommanders=0
bNoMonsters=True
bHumansOnly=False
bCoopWeaponMode=False
bClassicDeathMessages=False

[UTMenu.UTMenuBotmatchCW]
Map=DM-Deck16][.unr
GameType=BotPack.DeathMatchPlus
MutatorList=
bKeepMutators=False

[Botpack.TDMmaplist]
Maps[0]=DM-Codex.unr
Maps[1]=DM-turbine.unr
Maps[2]=DM-Phobos.unr
Maps[3]=DM-barricade.unr
Maps[4]=DM-Liandri.unr
Maps[5]=DM-Morpheus.unr
Maps[6]=DM-Gothic.unr
Maps[7]=DM-Tempest.unr
Maps[8]=DM-HyperBlast.unr
Maps[9]=DM-Grinder.unr
Maps[10]=DM-Kgalleon.unr
Maps[11]=DM-Zeto.unr
Maps[12]=DM-Pressure.unr
Maps[13]=DM-Conveyor.unr
Maps[14]=DM-Peak.unr
Maps[15]=DM-Curse][.unr
Maps[16]=DM-Deck16][.unr
Maps[17]=
Maps[18]=
Maps[19]=
Maps[20]=
Maps[21]=
Maps[22]=
Maps[23]=
Maps[24]=
Maps[25]=
Maps[26]=
Maps[27]=
Maps[28]=
Maps[29]=
Maps[30]=
Maps[31]=
MapNum=0

[UTMenu.UTServerSetupPage]
bLanPlay=True

[UTMenu.UTStartGameCW]
Map=DM-Deck16][.unr
GameType=BotPack.DeathMatchPlus
MutatorList=
bKeepMutators=False

[UMenu.UMenuNetworkClientWindow]
bShownWindow=True

[UBrowser.UBrowserOpenCW]
OpenHistory[0]=10.21.37.2
OpenHistory[1]=127.0.0.1
OpenHistory[2]=
OpenHistory[3]=
OpenHistory[4]=
OpenHistory[5]=
OpenHistory[6]=
OpenHistory[7]=
OpenHistory[8]=
OpenHistory[9]=
""".strip()

user_ini_content = """
[DefaultPlayer]
Name=Player
Class=Botpack.TMale2
team=255
skin=SoldierSkins.blkt
Face=SoldierSkins.Othello

[Engine.Input]
Aliases[0]=(Command="Button bFire | Fire",Alias=Fire)
Aliases[1]=(Command="Button bAltFire | AltFire",Alias=AltFire)
Aliases[2]=(Command="Axis aBaseY  Speed=+300.0",Alias=MoveForward)
Aliases[3]=(Command="Axis aBaseY  Speed=-300.0",Alias=MoveBackward)
Aliases[4]=(Command="Axis aBaseX Speed=-150.0",Alias=TurnLeft)
Aliases[5]=(Command="Axis aBaseX  Speed=+150.0",Alias=TurnRight)
Aliases[6]=(Command="Axis aStrafe Speed=-300.0",Alias=StrafeLeft)
Aliases[7]=(Command="Axis aStrafe Speed=+300.0",Alias=StrafeRight)
Aliases[8]=(Command="Jump | Axis aUp Speed=+300.0",Alias=Jump)
Aliases[9]=(Command="Button bDuck | Axis aUp Speed=-300.0",Alias=Duck)
Aliases[10]=(Command="Button bLook",Alias=Look)
Aliases[11]=(Command="Toggle bLook",Alias=LookToggle)
Aliases[12]=(Command="ActivateItem",Alias=InventoryActivate)
Aliases[13]=(Command="NextItem",Alias=InventoryNext)
Aliases[14]=(Command="PrevItem",Alias=InventoryPrevious)
Aliases[15]=(Command="Axis aLookUp Speed=+100.0",Alias=LookUp)
Aliases[16]=(Command="Axis aLookUp Speed=-100.0",Alias=LookDown)
Aliases[17]=(Command="Button bSnapLevel",Alias=CenterView)
Aliases[18]=(Command="Button bRun",Alias=Walking)
Aliases[19]=(Command="Button bStrafe",Alias=Strafe)
Aliases[20]=(Command="NextWeapon",Alias=NextWeapon)
Aliases[21]=(Command="ActivateTranslator",Alias=ActivateTranslator)
Aliases[22]=(Command="ActivateHint",Alias=ActivateHint)
Aliases[23]=(Command="Button bFreeLook",Alias=FreeLook)
Aliases[24]=(Command="ViewClass Pawn",Alias=ViewTeam)
Aliases[25]=(Command="",Alias=None)
Aliases[26]=(Command="",Alias=None)
Aliases[27]=(Command="",Alias=None)
Aliases[28]=(Command="",Alias=None)
Aliases[29]=(Command="",Alias=None)
Aliases[30]=(Command="",Alias=None)
Aliases[31]=(Command="",Alias=None)
Aliases[32]=(Command="",Alias=None)
Aliases[33]=(Command="",Alias=None)
Aliases[34]=(Command="",Alias=None)
Aliases[35]=(Command="",Alias=None)
Aliases[36]=(Command="",Alias=None)
Aliases[37]=(Command="",Alias=None)
Aliases[38]=(Command="",Alias=None)
Aliases[39]=(Command="",Alias=None)
LeftMouse=Fire
RightMouse=AltFire
MiddleMouse=MoveForward
Tab=Type
Enter=InventoryActivate
Shift=Walking
Ctrl=Jump
Alt=Fire
Pause=Pause
CapsLock=LookToggle
Escape=ShowMenu
Space=Jump
PageDown=LookDown
End=CenterView
Left=StrafeLeft
Up=MoveForward
Right=StrafeRight
Down=MoveBackward
Insert=
Delete=LookUp
0=SwitchWeapon 10
1=SwitchWeapon 1
2=SwitchWeapon 2
3=SwitchWeapon 3
4=SwitchWeapon 4
5=SwitchWeapon 5
6=SwitchWeapon 6
7=SwitchWeapon 7
8=SwitchWeapon 8
9=SwitchWeapon 9
C=Duck
G=Grab
L=Taunt wave
M=Look
O=Toggle bExtra0
S=Axis aUp Speed=+300.0
T=Talk
Z=Strafe
F1=ShowScores
F2=ShowServerInfo
F3=ShowObjectives
F4=
F5=ViewTeam
F6=Stat Net
F7=
F8=
F9=SShot
F10=Cancel
F11=Brightness
F12=EndFullscreen
Equals=GrowHUD
Comma=StrafeLeft
Minus=ShrinkHUD
Period=StrafeRight
Slash=NextWeapon
LeftBracket=InventoryPrevious
Backslash=ChangeHud
RightBracket=InventoryNext
MouseX=Axis aMouseX Speed=6.0
MouseY=Axis aMouseY Speed=6.0
MouseW=
None=
Cancel=
Backspace=
PageUp=
home=
Select=
Print=
Execute=
PrintScrn=SShot
Help=
A=
B=
D=
E=
f=Feigndeath
H=Taunt Thrust
i=
j=Taunt Taunt1
K=Taunt Victory1
P=
Q=GetWeapon BotPack.Translocator
R=TeamTalk
U=
V=
W=
X=
NumPad0=ViewPlayerNum 0
NumPad1=ViewPlayerNum 1
NumPad2=ViewPlayerNum 2
NumPad3=ViewPlayerNum 3
NumPad4=ViewPlayerNum 4
NumPad5=ViewPlayerNum 5
NumPad6=ViewPlayerNum 6
NumPad7=ViewPlayerNum 7
NumPad8=ViewPlayerNum 8
NumPad9=ViewPlayerNum 9
GreyStar=
Separator=
NumPadPeriod=Duck
GreySlash=
F13=
F14=
F15=
F16=
F17=
F18=
F19=
F20=
F21=
F22=
F23=
F24=
NumLock=
ScrollLock=
LShift=
RShift=
LControl=
RControl=
Semicolon=ThrowWeapon
Tilde=
SingleQuote=Strafe
Attn=
CrSel=
ExSel=
ErEof=
Play=
Zoom=
NoName=
PA1=
OemClear=
MouseZ=
MouseWheelDown=NextWeapon
MouseWheelUp=PrevWeapon
Joy1=Fire
Joy2=Jump
Joy3=AltFire
Joy4=Duck
Joy5=NextWeapon
Joy6=SwitchWeapon 2
Joy7=SwitchWeapon 3
Joy8=SwitchWeapon 4
Joy9=SwitchWeapon 9
Joy10=SwitchWeapon 0
Joy11=InventoryPrevious
Joy12=InventoryActivate
Joy13=InventoryNext
Joy14=
Joy15=
Joy16=
JoyX=Axis astrafe speed=2
JoyY=Axis aBaseY speed=2
JoyZ=
JoyR=
JoyU=Axis aturn speed=5.9
JoyV=Axis aLookUp speed=-3
JoyPovRight=SwitchWeapon 6
JoyPovLeft=SwitchWeapon 7
JoyPovUp=SwitchWeapon 8
JoyPovDown=SwitchWeapon 5

[Engine.PlayerPawn]
WeaponPriority[0]=Translocator
WeaponPriority[1]=ChainSaw
WeaponPriority[2]=ImpactHammer
WeaponPriority[3]=enforcer
WeaponPriority[4]=doubleenforcer
WeaponPriority[5]=ShockRifle
WeaponPriority[6]=ut_biorifle
WeaponPriority[7]=PulseGun
WeaponPriority[8]=SniperRifle
WeaponPriority[9]=ripper
WeaponPriority[10]=minigun2
WeaponPriority[11]=UT_FlakCannon
WeaponPriority[12]=UT_Eightball
WeaponPriority[13]=WarheadLauncher
WeaponPriority[14]=None
WeaponPriority[15]=None
WeaponPriority[16]=None
WeaponPriority[17]=None
WeaponPriority[18]=None
WeaponPriority[19]=None
Password=
DodgeClickTime=0.250000
Bob=0.016000
DesiredFOV=90.000000
DefaultFOV=90.000000
MyAutoAim=1.000000
Handedness=-1.000000
bLookUpStairs=False
bSnapToLevel=False
bAlwaysMouseLook=True
bKeyboardLook=True
bInvertMouse=False
bMaxMouseSmoothing=True
bNoFlash=True
bNoVoices=False
bMessageBeep=True
bNeverAutoSwitch=False
MouseSensitivity=3.000000
WeaponPriority[20]=None
WeaponPriority[21]=None
WeaponPriority[22]=None
WeaponPriority[23]=None
WeaponPriority[24]=None
WeaponPriority[25]=None
WeaponPriority[26]=None
WeaponPriority[27]=None
WeaponPriority[28]=None
WeaponPriority[29]=None
WeaponPriority[30]=None
WeaponPriority[31]=None
WeaponPriority[32]=None
WeaponPriority[33]=None
WeaponPriority[34]=None
WeaponPriority[35]=None
WeaponPriority[36]=None
WeaponPriority[37]=None
WeaponPriority[38]=None
WeaponPriority[39]=None
WeaponPriority[40]=None
WeaponPriority[41]=None
WeaponPriority[42]=None
WeaponPriority[43]=None
WeaponPriority[44]=None
WeaponPriority[45]=None
WeaponPriority[46]=None
WeaponPriority[47]=None
WeaponPriority[48]=None
WeaponPriority[49]=None
MouseSmoothThreshold=0.070000
MaxTimeMargin=3.000000
ngWorldSecret=
ngSecretSet=False

[Engine.HUD]
HudMode=0	
Crosshair=0

[Botpack.ChallengeHUD]
bUseTeamColor=true
FavoriteHUDColor=(R=0,G=0,B=16)
CrosshairColor=(R=0,G=16,B=0)
HudScale=+1.0
Opacity=15
StatusScale=1.0
WeaponScale=0.8
bHideAllWeapons=false
bHideStatus=false
bHideAmmo=false
bHideTeamInfo=false
bHideFrags=false
bHideHUD=false
bHideNoviceMessages=false
bHideFaces=false

[Botpack.ChallengeBotInfo]
BotFaces[0]=CommandoSkins.Blake
BotFaces[1]=SGirlSkins.Aryss
BotFaces[2]=SoldierSkins.Malcom
BotFaces[3]=CommandoSkins.Luthor
BotFaces[4]=FCommandoSkins.Cryss
BotFaces[5]=FCommandoSkins.Visse
BotFaces[6]=SoldierSkins.Kregore
BotFaces[7]=SGirlSkins.Cilia
BotFaces[8]=CommandoSkins.Kragoth
BotFaces[9]=FCommandoSkins.Tanya
BotFaces[10]=SoldierSkins.Johnson
BotFaces[11]=CommandoSkins.Boris
BotFaces[12]=SGirlSkins.Vixen
BotFaces[13]=SGirlSkins.Sara
BotFaces[14]=SoldierSkins.Othello
BotFaces[15]=FCommandoSkins.Kyla
BotFaces[16]=CommandoSkins.Gorn
BotFaces[17]=SGirlSkins.Annaka
BotFaces[18]=SoldierSkins.Riker
BotFaces[19]=FCommandoSkins.Malise
BotFaces[20]=CommandoSkins.Ramirez
BotFaces[21]=FCommandoSkins.Freylis
BotFaces[22]=SoldierSkins.Arkon
BotFaces[23]=SGirlSkins.Sarena
BotFaces[24]=CommandoSkins.Grail
BotFaces[25]=FCommandoSkins.Mariana
BotFaces[26]=SoldierSkins.Rankin
BotFaces[27]=SGirlSkins.Isis
BotFaces[28]=CommandoSkins.Graves
BotFaces[29]=SGirlSkins.Lauren
BotFaces[30]=SoldierSkins.Malcom
BotFaces[31]=FCommandoSkins.Jayce
bAdjustSkill=False
bRandomOrder=True
Difficulty=1
BotNames[0]=Archon
BotNames[1]=Aryss
BotNames[2]=Alarik
BotNames[3]=Dessloch
BotNames[4]=Cryss
BotNames[5]=Nikita
BotNames[6]=Drimacus
BotNames[7]=Rhea
BotNames[8]=Raynor
BotNames[9]=Kira
BotNames[10]=Karag
BotNames[11]=Zenith
BotNames[12]=Cali
BotNames[13]=Alys
BotNames[14]=Kosak
BotNames[15]=Illana
BotNames[16]=Barak
BotNames[17]=Kara
BotNames[18]=Tamerlane
BotNames[19]=Arachne
BotNames[20]=Liche
BotNames[21]=Jared
BotNames[22]=Ichthys
BotNames[23]=Tamara
BotNames[24]=Loque
BotNames[25]=Athena
BotNames[26]=Cilia
BotNames[27]=Sarena
BotNames[28]=Malakai
BotNames[29]=Visse
BotNames[30]=Necroth
BotNames[31]=Kragoth
BotTeams[0]=255
BotTeams[1]=0
BotTeams[2]=255
BotTeams[3]=1
BotTeams[4]=255
BotTeams[5]=2
BotTeams[6]=255
BotTeams[7]=3
BotTeams[8]=255
BotTeams[9]=0
BotTeams[10]=255
BotTeams[11]=1
BotTeams[12]=255
BotTeams[13]=2
BotTeams[14]=255
BotTeams[15]=3
BotTeams[16]=255
BotTeams[17]=0
BotTeams[18]=255
BotTeams[19]=1
BotTeams[20]=255
BotTeams[21]=2
BotTeams[22]=255
BotTeams[23]=3
BotTeams[24]=255
BotTeams[25]=0
BotTeams[26]=255
BotTeams[27]=1
BotTeams[28]=255
BotTeams[29]=2
BotTeams[30]=255
BotTeams[31]=3
BotClasses[0]=BotPack.TMale1Bot
BotClasses[1]=BotPack.TFemale2Bot
BotClasses[2]=BotPack.TMale2Bot
BotClasses[3]=BotPack.TMale1Bot
BotClasses[4]=BotPack.TFemale1Bot
BotClasses[5]=BotPack.TFemale1Bot
BotClasses[6]=BotPack.TMale2Bot
BotClasses[7]=BotPack.TFemale2Bot
BotClasses[8]=BotPack.TMale1Bot
BotClasses[9]=BotPack.TFemale1Bot
BotClasses[10]=BotPack.TMale2Bot
BotClasses[11]=BotPack.TMale1Bot
BotClasses[12]=BotPack.TFemale2Bot
BotClasses[13]=BotPack.TFemale2Bot
BotClasses[14]=BotPack.TMale2Bot
BotClasses[15]=BotPack.TFemale1Bot
BotClasses[16]=BotPack.TMale1Bot
BotClasses[17]=BotPack.TFemale2Bot
BotClasses[18]=BotPack.TMale2Bot
BotClasses[19]=BotPack.TFemale1Bot
BotClasses[20]=BotPack.TMale1Bot
BotClasses[21]=BotPack.TFemale1Bot
BotClasses[22]=BotPack.TMale2Bot
BotClasses[23]=BotPack.TFemale2Bot
BotClasses[24]=BotPack.TMale1Bot
BotClasses[25]=BotPack.TFemale1Bot
BotClasses[26]=BotPack.TMale2Bot
BotClasses[27]=BotPack.TFemale2Bot
BotClasses[28]=BotPack.TMale1Bot
BotClasses[29]=BotPack.TFemale2Bot
BotClasses[30]=BotPack.TMale2Bot
BotClasses[31]=BotPack.TFemale1Bot
BotSkins[0]=CommandoSkins.cmdo
BotSkins[1]=SGirlSkins.fbth
BotSkins[2]=SoldierSkins.blkt
BotSkins[3]=CommandoSkins.daco
BotSkins[4]=FCommandoSkins.goth
BotSkins[5]=FCommandoSkins.goth
BotSkins[6]=SoldierSkins.RawS
BotSkins[7]=SGirlSkins.Venm
BotSkins[8]=CommandoSkins.goth
BotSkins[9]=FCommandoSkins.daco
BotSkins[10]=SoldierSkins.sldr
BotSkins[11]=CommandoSkins.daco
BotSkins[12]=SGirlSkins.Garf
BotSkins[13]=SGirlSkins.army
BotSkins[14]=SoldierSkins.blkt
BotSkins[15]=FCommandoSkins.daco
BotSkins[16]=CommandoSkins.cmdo
BotSkins[17]=SGirlSkins.fbth
BotSkins[18]=SoldierSkins.blkt
BotSkins[19]=FCommandoSkins.goth
BotSkins[20]=CommandoSkins.daco
BotSkins[21]=FCommandoSkins.goth
BotSkins[22]=SoldierSkins.RawS
BotSkins[23]=SGirlSkins.Venm
BotSkins[24]=CommandoSkins.goth
BotSkins[25]=FCommandoSkins.daco
BotSkins[26]=SoldierSkins.sldr
BotSkins[27]=SGirlSkins.Garf
BotSkins[28]=CommandoSkins.daco
BotSkins[29]=SGirlSkins.army
BotSkins[30]=SoldierSkins.blkt
BotSkins[31]=FCommandoSkins.daco

[Botpack.TournamentPlayer]
bInstantRocket=False
bAutoTaunt=False
bNoAutoTaunts=False
bNoVoiceTaunts=False
bNoMatureLanguage=False
bNoVoiceMessages=False
AnnouncerVolume=4

[Engine.Pawn]
bNeverSwitchOnPickup=False

""".strip()


def main():
    ini_path = os.getenv("HOME") + "/.loki/ut/System/UnrealTournament.ini"
    os.makedirs(os.path.dirname(ini_path), exist_ok=True)

    if not os.path.exists(ini_path):
        with open(ini_path, "wt") as f:
            f.write(ut_ini_content)

if __name__ == "__main__":
    main()