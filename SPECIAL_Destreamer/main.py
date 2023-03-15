import subprocess

ffmpeg_installed = False

try:
    process = subprocess.Popen("ffmpeg -version", stdout=subprocess.PIPE)
    out = process.stdout.read().splitlines()

    ffmpeg_installed = True
except:
    print("FFMPEG not installed")
    exit(-1)
finally:

    if ffmpeg_installed:
        try:
            file = open("links.txt", "r")
            links = file.readlines()
        except FileNotFoundError:
            print("links.txt not found")
            exit(-2)
        except:
            print("Something went wrong opening the links.txt file")
            exit(-3)
        finally:
            file.close()

            count = 0

            if len(links) == 0:
                print("No links found in links.txt")
                exit(-5)

            try:
                for link in links:
                    process = subprocess.Popen(f"ffmpeg -i \"{link}\" -codec copy video_{count + 1}.mp4", stdout=subprocess.PIPE)
                    out = process.stdout.read().splitlines()
                    print(out)
                    print(f"Processed video_{count + 1}.mp4")
                    count += 1
            except:
                print(f"Error processing video_{count + 1}.mp4")
                exit(-4)