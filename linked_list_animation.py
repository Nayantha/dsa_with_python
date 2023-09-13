from manim import *
import numpy as np

class SinglyLinkedList(VGroup):
    def __init__(self, content="None"):
        super().__init__()
        self.sq = Rectangle(width=3)
        self.pt = Rectangle(width=3,height=1)
        self.back = Circle(radius=0)
        self.content = Text(content)
        self.add(self.sq,self.content, self.pt, self.back)
        self.pt.shift(DOWN*(self.sq.height/2+self.pt.height/2))
        self.content.move_to(self.get_center())
        self.back.move_to(self.pt.get_edge_center(LEFT))
        self.arrow = None
        self.next_node = None
        self.add(SinglyLinkedList())

class SinglyLinkedListScene(Scene):
    def construct(self):
        singly_linked_list = SinglyLinkedList()
        self.play(Write(singly_linked_list))
