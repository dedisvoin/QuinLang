from GLib.mathematics import *
from GLib.drawing import *

def collide_two_rect(r1_pos, r1_size, r2_pos, r2_size):
        
        min_x = min(r1_pos[0], r2_pos[0])
        min_y = min(r1_pos[1], r2_pos[1])

        max_x = max(r1_pos[0] + r1_size[0], r2_pos[0] + r2_size[0])
        max_y = max(r1_pos[1] + r1_size[1], r2_pos[1] + r2_size[1])

        dist_w = distance([min_x, min_y], [max_x, min_y])
        dist_h = distance([min_x, min_y], [min_x, max_y])
        
        #Draw.draw_rect(win.surf, [min_x, min_y], [dist_w, dist_h], 'red',1)
        if dist_w < r1_size[0] + r2_size[0] and dist_h < r1_size[1] + r2_size[1]:
            return True
        return False

class BoxTypes:
         STATICK = 'statick'
         DYNAMIC = 'dynamic'

class Physics:
    def __init__(self) -> None:
          pass

    class BoxCollider:
        def __init__(self,
                      pos,
                      size,
                      type: BoxTypes = BoxTypes.STATICK,
                      *,
                      speed: Vector2 = Vector2(0, 0),
                      bounsing: Vector2 = Vector2(0.5,0.5),
                      duration: Vector2 = Vector2(0.5,0.5),
                      air_friction: Vector2 = Vector2(0.95,1),
                      id: str = None,
                      ) -> None:
            
            self.pos = Vector2(pos)
            self.speed = speed
            self.size = size
            self.type = type
            self.bounsing = bounsing
            self.duration = duration
            self.air_friction = air_friction
            self.id = id
            if self.id is None:
                 self.id = random.randint(0,9999999999999)
        
            self.collides = {
                'up': False,
                'down':False,
                'left':False,
                'right': False
            }

        def set_default_collides(self):
            self.collides = {
                'up': False,
                'down':False,
                'left':False,
                'right': False
            }
        
        @property
        def center(self):
            return center_rect(self.pos.xy, self.size)

        @property
        def up(self):
            return self.pos.y
        
        @property
        def down(self):
            return self.pos.y+self.size[1]
        
        @property
        def left(self):
            return self.pos.x
        
        @property
        def right(self):
            return self.pos.x+self.size[0]
        
        @up.setter
        def up(self, y):
            self.pos.y = y
        
        @down.setter
        def down(self, y):
            self.pos.y = y-self.size[1]
        
        @left.setter
        def left(self, x):
            self.pos.x = x
        
        @right.setter
        def right(self, x):
            self.pos.x = x-self.size[0]
    
    class Space:
        GRAVITY = Vector2(0,0.8)
        MAX_Y = 20
        MAX_X = 20

        def __init__(self) -> None:
            self.colliders = []

        def add(self, colliders: list):
             self.colliders+=colliders

        def get_all_collides(self, collider):
            collide_rects = []

            for collider2 in self.colliders:
                if collider2.id != collider.id:
                    if collide_two_rect(collider.pos.xy, collider.size, collider2.pos.xy, collider2.size):
                         collide_rects.append(collider2)

            return collide_rects
        
        def view(self, win, camera):
            for rect in self.colliders:
                Draw.draw_rect(win.surf, [rect.pos.x+camera.pos[0], rect.pos.y+camera.pos[1]], rect.size, (255,200,200))

        
        def get_by_id(self, id):
            for rect in self.colliders:
                if rect.id == id:
                    return rect
                         

        def update(self):

            for collider in self.colliders:
                


                if collider.type == BoxTypes.DYNAMIC:
                    collider.speed.y*=collider.air_friction.y
                    collider.speed.x*=collider.air_friction.x

                    collider.set_default_collides()
                    collider.speed.y = min(collider.speed.y, self.MAX_Y)
                    collider.speed.y = max(collider.speed.y, -self.MAX_Y)

                    collider.speed.y+=self.GRAVITY.y
                    collider.pos.y+=collider.speed.y
                    collide_rects = self.get_all_collides(collider)

                    for rect in collide_rects:
                        #rect.speed.y = copy((collider.speed.y+rect.speed.y))

                        if collider.center[1]>rect.center[1]:
                            collider.collides['up'] = True
                            collider.up = rect.down
                            collider.speed.y*=-collider.bounsing.y
                            collider.speed.x*=rect.duration.x
                        if collider.center[1]<rect.center[1]:
                            collider.collides['down'] = True
                            collider.down = rect.up  
                            collider.speed.y*=-collider.bounsing.y
                            collider.speed.x*=rect.duration.x
                        

                    collider.speed.x+=self.GRAVITY.x
                    collider.pos.x+=collider.speed.x
                    collide_rects = self.get_all_collides(collider)

                    for rect in collide_rects:
                        #rect.speed.x = copy((collider.speed.x+rect.speed.x))

                        if collider.center[0]>rect.center[0]:
                            collider.collides['left'] = True
                            collider.left = rect.right
                            collider.speed.x*=-collider.bounsing.x
                            collider.speed.y*=rect.duration.y
                        if collider.center[0]<rect.center[0]:
                            collider.collides['right'] = True
                            collider.right = rect.left  
                            collider.speed.x*=-collider.bounsing.x
                            collider.speed.y*=rect.duration.y


                  
                  

        
  
