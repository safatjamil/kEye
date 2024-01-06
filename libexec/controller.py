import sys
import argparse

class Handler:
    def response(self, data):
        print(data["message"])
        