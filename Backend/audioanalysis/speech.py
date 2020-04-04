from audioanalysis import myspsolution as mysp

# path to the file's directory
def run_overview(file_title, file_location=r"/home/logan/FCRWebApp/Backend/audioanalysis/test_files"):
    print("Running analysis on " + file_location+"/"+file_title)
    mysp.mysptotal(file_title, file_location)
