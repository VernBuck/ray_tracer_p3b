# This is the starter code for the CS 3451 Ray Tracing project.
#
# The most important part of this code is the interpreter, which will
# help you parse the scene description (.cli) files.
#from intersection_point import *
from light import *
from sphereM import *
from surface_material import *
from ray import *
from intersection_point import *
from later_triangle import *
#from shadow import *

global backgroundObject
global lightsource
lightsource = []
global surfaceV
global allShapes
allShapes = []
global fov_saved
#global fovlist 
#fovlist = []


def setup():
    size(200, 200) 
    noStroke()
    colorMode(RGB, 1.0)  # Processing color values will be in [0, 1]  (not 255)
    background(0, 0, 0)

# read and interpret the appropriate scene description .cli file based on key press
def keyPressed():
    if key == '1':
        interpreter("i1.cli")
    elif key == '2':
        interpreter("i2.cli")
    elif key == '3':
        interpreter("i3.cli")
    elif key == '4':
        interpreter("i4.cli")
    elif key == '5':
        interpreter("i5.cli")
    elif key == '6':
        interpreter("i6.cli")
    elif key == '7':
        interpreter("i7.cli")
    elif key == '8':
        interpreter("i8.cli")
    elif key == '9':
        interpreter("i9.cli")

def interpreter(fname):
    global lightsource
    lightsource = []
    global allShapes
    allShapes= []
    global backgroundObject
    backgroundObject = None
    global surfaceV
    fname = "data/" + fname
    # read in the lines of a file
    with open(fname) as f:
        lines = f.readlines()

    # parse each line in the file in turn
    for line in lines:
        words = line.split()  # split the line into individual tokens
        if len(words) == 0:   # skip empty lines
            continue
        if words[0] == 'sphere': #done
            radius = float(words[1])
            x = float(words[2])
            y = float(words[3])
            z = float(words[4])
            textShape = 'sphere'
            item = sphereM(x,y,z,textShape,radius,surfaceV)
            allShapes.append(item)
        if words[0] == 'rect':
            p1 = float(words[1])
            p2 = float(words[2])
            p3 = float(words[3])
            p4 = float(words[4])
            #need to make a rectangle holder
            #need to place points in rectangle holder
        elif words[0] == 'fov': #done
            global fov_saved
            fov_saved = float(words[1])
            pass
        elif words[0] == 'background': #done
            #store background color after reading file
            r = float(words[1])
            g = float(words[2])
            b = float(words[3])
            global backgroundObject
            backgroundObject = color(r, g, b) 
            pass
        elif words[0] == 'light': #done
            x = float(words[1])
            y = float(words[2])
            z = float(words[3])
            r = float(words[4])
            g = float(words[5])
            b = float(words[6])
            item = light(x,y,z,r,g,b)
            lightsource.append(item)
            pass
        elif words[0] == 'surface': #done
            Crd = float(words[1])
            Cdg = float(words[2])
            Cdb = float(words[3])
            Car = float(words[4])
            Cag = float(words[5])
            Cab = float(words[6])
            Csr = float(words[7])
            Csg = float(words[8])
            Csb = float(words[9])
            P = float(words[10])
            Krefl = float(words[11])
            surfaceV = surface_material(Crd,Cdg,Cdb,Car,Cag,Cab,Csr, Csg, Csb, P, Krefl)
            pass
        elif words[0] == 'begin': #done should be for next homework though
            #create a list to hold all vertex
            global vertList
            vertList = []
            pass
        elif words[0] == 'vertex': #next homework
            p1 = float(words[1])
            p2 = float(words[2])
            p3 = float(words[3])
            #appending to the list 3 vertex commands
            #listVertex = [p1,p2,p3]
            triDir = PVector(p1,p2,p3)
            vertList.append(triDir)
            
            pass
        elif words[0] == 'end': #next homework
            #see vertex pt into triangle object
            #draws object
            textShape = 'triangle'
            item = later_triangle(vertList[0],vertList[1],vertList[2], textShape, surfaceV)
            allShapes.append(item)
            pass
        elif words[0] == 'write':
            render_scene()    # render the scene
            save(words[1])  # write the image to a file
            pass

# render the ray tracing scene
def render_scene():
    global backgroundObject
    k = tan(radians(fov_saved)/2)
    for j in range(height):
        for i in range(width):
            x = (i - width / 2) * 2 * k/width 
            y = (j - width/ 2) * 2 * k/width 
            z = -1
            varDir = PVector(x,y,z)
            ray1 = ray (PVector(0,0,0), varDir.normalize())
            #shadow code here
            #use point of intersection with an object and light
            intersectCalc = None
            valueOfI= 0
            for p in range(0,len(allShapes)):
                lowestMin = intersection_point(ray1, allShapes[p], 0, True, 0, 0, 0) #t value
                if (lowestMin.bool and (intersectCalc is None or lowestMin.minVal < intersectCalc.minVal)):
                    intersectCalc = lowestMin   
                    valueOfI = p
            
            if (intersectCalc == None):
                if (backgroundObject == None):
                    pix_color = color(0,0,0)
                else:
                    pix_color = backgroundObject
                    
            else:
                
                #R(t) = t * (dx, dy, dz) = n
                #work on specular and shadow next
                Rtx = intersectCalc.minVal * intersectCalc.dx
                Rty = intersectCalc.minVal * intersectCalc.dy
                Rtz = intersectCalc.minVal * intersectCalc.dz
                
                # intersectCalc lowestMin
                shadowXDir = intersectCalc.dx
                shadowYDir = intersectCalc.dy
                shadowZDir = intersectCalc.dz
                
                finalR = 0#surfaceV.Car #set to ambient
                finalG = 0#surfaceV.Cag #set to ambient
                finalB = 0#surfaceV.Cab #set to ambient
                #what do I do with the specular values
                #where should I start the recursion for mirror
                #
                interSectionPoint = PVector(Rtx,Rty,Rtz)
                n = allShapes[valueOfI].normalS(interSectionPoint).normalize()
                objectSurface = allShapes[valueOfI].surfacematerial
                #shadow make a ray from intersection point to light then pass it into intersection!
                
                                
                
                
                #for p in range(0,len(allShapes)):
                    #if (shadowBool == True):
                        
    
                
                                        
                ambCR = objectSurface.Car
                ambCG = objectSurface.Cag
                ambCB = objectSurface.Cab 
                diffCR = 0
                diffCG = 0
                diffCB = 0
                specR = 0 
                specG = 0
                specB = 0
                
                for p in range(0, len(lightsource)):
                    #lightVector = (intersectCalc, lightsource[p])
                    
                    LightPos = PVector(lightsource[p].x,lightsource[p].y, lightsource[p].z)  
                    
                    shadow = ray(interSectionPoint, LightPos)
                    shadowBool = intersection_point(shadow, allShapes[p], 0, True, 0, 0, 0)
                    if(shadowBool == True and !allShapes[p]):
                        pix_color = color(0, 0, 0)
                        specR = 0
                        specG = 0
                        specB = 0
                        diffCR = 0
                        diffCG = 0
                        diffCB = 0
                        ambCR = 0
                        ambCG = 0
                        diffCB = 0
                        
                        
                    else:
                     #normalVector
                        L = (LightPos - interSectionPoint).normalize()
                    #println(n)
                    #println(L)
                    #println(PVector.dot(n,L))
                    #R = 2*n * (n*L) - L
                    #E = PVector(0,0,0) - lowestMin
                    #max(0, PVector(
                    #book spectral equation
                        reverseR = ray1.starting_point - ray1.direction
                        h = (reverseR + L).normalize()
                        specR += objectSurface.Csr * max(0, PVector.dot(h, n)) ** (objectSurface.P)  
                        specG += objectSurface.Csg * max(0, PVector.dot(h, n)) ** (objectSurface.P)  
                        specB += objectSurface.Csb * max(0, PVector.dot(h, n)) ** (objectSurface.P) 
                    
            
                        diffCR += lightsource[p].r * max(0,PVector.dot(n,L)) #* surfaceV.Crd #+ specR  # multiply by specular
                        diffCG += lightsource[p].g * max(0,PVector.dot(n,L)) #* surfaceV.Cdg #+ specG # multiply by specular
                        diffCB += lightsource[p].b * max(0,PVector.dot(n,L)) #* surfaceV.Cdb#+ specB # multiply by specular
                        
                finalR2 = ambCR + diffCR * objectSurface.Crd + specR 
                finalG2 = ambCG + diffCG * objectSurface.Cdg + specG 
                finalB2 = ambCB + diffCB * objectSurface.Cdb + specB 
                
                
                
                pix_color = color(finalR2, finalG2, finalB2)  # you should calculate the correct pixel color here                    
            set (i, height - j, pix_color)         # fill the pixel with the calculated color
    print("finished")
    pass
def vectorCalc(Lightsource, LightIndex, allShapes, allShapesIndex, Rtx, Rty, Rtz):
        finalR += lightsource[p].r * max(0,PVector.dot(((PVector(lightsource[p].x, lightsource[p].y, lightsource[p].z) - PVector(allShapes[p].x, allShapes[p].y, allShapes[p].z))*PVector(Rtx, Rty, Rtz))))

# should remain empty for this assignment
def draw():
    pass