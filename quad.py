#!/usr/bin/env python
# -*- coding: latin-1 -*-

import sys, time, math, os, random
sys.path.insert(0, 'Shared')
sys.path.insert(0, 'Shaders')
from   pyglet.gl    import *
from   shader       import Shader
from   grammar      import *
from   stringparser import Parser
from   keys         import *
import subprocess
import pytumblr
import urllib
import threading

tumblrClient = pytumblr.TumblrRestClient(
    tumblr_consumer_key,
    tumblr_consumer_secret,
    tumblr_token_key,
    tumblr_token_secret
)

config     = Config( sample_buffers=1, samples=4, depth_size=16, double_buffer=True )
window     = pyglet.window.Window(resizable=True, config=config, vsync=False) # "vsync=False" to check the framerate
x          = 400
y          = 400
quad       = pyglet.graphics.vertex_list(4, ('v2f', [-x,-y, x,-y, -x,y, x,y]), ('t2f', [0,0, 1,0, 0,1, 1,1]))
window.set_size(x, y)

@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glPushMatrix()
    quad.draw(GL_TRIANGLE_STRIP)
    glPopMatrix()


def setup():
    random.seed()
    seed = int( time.time() )
    os.mkdir( "Output/" + str( seed ) )
    pyglet.clock.tick()
    return seed

def getGeneratedFragment():
    with open ("shaders/basicfrag.glsl", "r") as fragfile:
        frag = fragfile.read()

    grammar["shader"] = [ frag ]
    parser = Parser( grammar )
    frag   = parser.Parse( "shader" )
    return frag


def getShader( frag, seed ):
    with open ("shaders/basicvert.glsl", "r") as vertfile:
      vert = vertfile.read()

    with open ("shaders/noise.glsl", "r") as noisefile:
      noise = noisefile.read()

    with open ("shaders/utils.glsl", "r") as utilsfile:
      utils = utilsfile.read()

    with open ("shaders/header.glsl", "r") as headerfile:
      header = headerfile.read()

    fullfrag = header + noise + utils + frag

    with open( "Output/" + str( seed ) + "/" + str( seed ) + ".glsl", "w") as text_file:
        text_file.write( frag )

    with open( "Output/" + str( seed ) + "/" + str( seed ) + "full.glsl", "w") as text_file:
        text_file.write( fullfrag )

    shader = Shader( vert, fullfrag )
    shader.bind()
    shader.uniformf( "iResolution", x, y )
    return shader

def postToPastebin( code, seed ):
    pastebin_session_vars = {
        'api_dev_key'      : pastebin_key,
        'api_user_name'    : pastebin_user,
        'api_user_password': pastebin_pass } 
    response = urllib.urlopen('http://pastebin.com/api/api_login.php', urllib.urlencode(pastebin_session_vars))
    session  = response.read()
    print "Pastebin session:" + session

    pastebin_post_vars = {
        'api_dev_key'       : pastebin_key,
        'api_option'        :'paste',
        'api_paste_code'    : code,
        'api_user_key'      : session,
        'api_paste_name'    : str( seed ) + '.glsl',
        'api_paste_format'  : 'glsl',
        'api_paste_private' : 0 } 
    response = urllib.urlopen('http://pastebin.com/api/api_post.php', urllib.urlencode(pastebin_post_vars))
    url = response.read()
    print "Posted to pastebin as:" + url
    return url

def postToTumblr( url, filename, seed ):
    lasttag = [ "test", "art", "art?", "professional", "real art", "emotions", "colour", "bot", 
                "i made this", "definitely art", "bad art", "oh no", "awkward", "brands", "hashtag",
                "imperfect loop", "rainbow", "python", "pro", "very good", u"¯\_(ツ)_/¯", "maths",
                "determinism", "retrofuturism", "serious", "coder art", "opengl", "loud noises",
                "me_irl", "gif", "pastebin", "source code", "shadertoy", "infinite", "terrible",
                "programmer", "grammar", "mistake", "SIGNALxNOISE", "words", "void", "hsv", "rgb", ":)" ]
    tags = [ "generative", "noise", "signal", "perlin", "simplex", "shader", "glsl" ] 
    tags = tags + random.sample( lasttag, random.randint( 1, 3 ) ) 
    random.shuffle( tags )
    text = '<b>' + str( seed ) +'.glsl</b><br /><a href="' + url + '">source code</a>'
    tumblrClient.create_photo('signalxnoise', caption=text, slug=str(seed) + "_dot_glsl", state="published", tags=tags, data=filename)
    print "Posted to tumblr"

def renderImage():
    seed   = setup()
    frag   = getGeneratedFragment()
    shader = getShader( frag, seed )
    frames = 10
    filenameList = []
    for window in pyglet.app.windows:
        window.switch_to()
        for i in range(0,frames + 3):
            window.dispatch_events()
            shader.uniformf( "iGlobalTime", i - 3 )
            window.dispatch_event('on_draw')
            window.flip()
            if i > 2:               
                filename = "Output/" + str( seed ) + "/" + str( i - 3 ) + ".png"
                pyglet.image.get_buffer_manager().get_color_buffer().save( filename )
                filenameList.append( filename )

    shader.unbind()
    shader.destroy()

    convertexepath = "Shared/convert.exe"
    animFilename   = "Output/" + str( seed ) + "/anim.gif"
    convertcommand = [convertexepath, "-delay", "15", "-size", str(window.width) + "x" + str(window.height)] + filenameList + [ animFilename ]
    subprocess.call(convertcommand)
    print "Gif created:" + animFilename

    pastebinURL = postToPastebin( shader.frag, seed )
    postToTumblr( pastebinURL, animFilename, seed )

sleeptime = 60*60
def runBot(): 
    info = tumblrClient.info()
    if "meta" in info and info[ "meta" ][ "status" ] != 200:
        print "tumblr auth failed"
        print  tumblrClient.info()
    else: 
        while 1:    
            print "beginning new image"
            renderImage();
            print "sleeping for " + str( sleeptime / 60 ) + " minutes"
            print ""
            time.sleep(sleeptime)

runBot()
#print "Posted to tumblr, response: " + str( tumblrClient.info()[ "meta" ][ "status" ] )
