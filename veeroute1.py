from lib.convertfiles import convertxlsxtojson

def main():
    try:
        convertxlsxtojson()
        return
    except Exception as err:
        print(err)

main()