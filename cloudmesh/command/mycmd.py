import cmd

class CMShell(cmd.Cmd):
    """Simple command processor example."""
    
    def do_deploy(self, line):
        print ("deploy" + line)

    def do_benchmark(self, line):
        print ("benchmark"+ line)

    def do_test(self, line):
        print ("test" + line)

    def do_run(self, line):
        print ("run" + line)
    
    def do_EOF(self, line):
        return True

def main():
    MyCmd().cmdloop()
    
if __name__ == '__main__':
    main()
