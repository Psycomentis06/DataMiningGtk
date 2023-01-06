'''
This a sample class contains an exemples which will not be loaded by default.
Use it as a reference to create your own extension.
do not forget to register it in the entry.json file located in $HOME/.datasets/
'''
class SampleDataset:
    def __init__(self, name: str,**kwargs) -> None:
        pass
    
    def getColumns(self):
        pass


