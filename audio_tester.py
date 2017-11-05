import os
os.system('curl -X POST -u 3d5b08b4-11f9-41ff-8616-a4151631ceca:XifktXRgSYbH --header "Content-Type: audio/wav" --header "Transfer-Encoding: chunked" --data-binary @test1.wav "https://stream.watsonplatform.net/speech-to-text/api/v1/recognize"')
