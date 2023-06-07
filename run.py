import os, json, time, ngrok_token

javaArgs = "-Xms512M -Xmx512M -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=8M -XX:G1ReservePercent=20 -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1 -Dusing.aikars.flags=https://mcflags.emc.gs -Daikars.new.flags=true" #https://aikar.co/2018/07/02/tuning-the-jvm-g1gc-garbage-collector-flags-for-minecraft/

try:
  import flask
except:
  os.system("pip3 install flask")
  import flask

installed = True
def write(filename,content):
  f = open(filename,"a")
  f.write("")
  f.close()
  f = open(filename,"w")
  f.write(str(content))
  f.close()

def run():
  os.system("./ngrok tcp 25565 >/dev/null &")
  time.sleep(1)
  os.system("curl http://localhost:4040/api/tunnels > tunnels.json")
  with open('tunnels.json') as data_file:
    try:
      datajson = json.load(data_file)
    except:
      print("")
  os.system("echo {url} > url.txt".format(url=datajson['tunnels'][-1]["public_url"].replace("tcp://","")))
  os.system("python3 webserver.py >/dev/null &")
  os.chdir("server")
  write("eula.txt","eula=true")
  os.system("java {javaArgs} -jar server.jar -nogui".format(javaArgs=javaArgs))

try:
  f = open("server-is-installed")
  f.close
except:
  installed = False

ngrok_token.refreshToken()

if installed == False:
  os.system("rm -r -f server")
  os.system("install-pkg openjdk-8-jre-headless")
  os.system("mkdir server")
  os.system("cp server.jar server/server.jar")
  write("server-is-installed","If this file is here, the server is installed. If you want to reinstall the server, then delete this file.")
  run()
else:
  run()