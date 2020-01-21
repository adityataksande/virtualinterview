import speech_recognition as sr  


# get audio from the microphone                                                                       
r = sr.Recognizer()                                                                                   
with sr.Microphone() as source: 
    print(" What are the basic data types associated with C?")                                                                      
    print("Say Your Answer:")                                                                                   
    audio = r.listen(source)   
    
def convert(usr): 
   return (usr[0].split()) 

def convert(ans):
    return(ans[0].split())

def intersection(ans,usr):
    lst3 = [value for value in ans if value in usr] 
    return lst3 
  

try:
    
    print("You said =" + r.recognize_google(audio))
    usr =  [r.recognize_google(audio)] 
    print(  convert(usr)) 
    ans =["Int Float Double Charecter void"]
    #print( convert(ans))
    #print(intersection(convert(usr),convert(ans) ))
    
    l= len(intersection(convert(usr),convert(ans) ));
    
    if l<=2:
        print("Your Answer is Partially Correct")
    elif l==0 :
        print("Your Answer is Wrong")
    else:
        print("Your Answer is Correct")

except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))

