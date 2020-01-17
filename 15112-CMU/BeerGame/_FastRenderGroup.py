#!/usr/bin/env python
#
#
#
#
#

"""
FastRenderGroup

VERSION: you get version information here as a string
VERSION_NUMBER: you get a tuple containing (release, subrelease, revision)
                so you can compare the numbers

changelog:
11.07.2007:
- pygame 1.8 feature blendmode activated, removed old code

07.07.2007: 
- renamed both groups to LayeredUpdates and LayeredDirty as suggested by illume
- made the _get_visible and _set_visible property such that they can be 
  overwritten.

05.07.2007: (v1.1.83)
- change the timing code to switch between modes (prolbem of finding the 
  treshold value is still there)
- set_timing_treshold() added
- LayeredRenderGroup.layers() now usese a set()

29.06.07: (v1.1.78)
- moved unittests to fastrendergroup_test.py
- cleaned up the code using pylint (still some strange things in here)
- docstrings should be complete,although perhaps not as clear as they should be
- testsprite.py modified to be able to test FastRenderGroup in there too
- written a multi_FRG_demo.py to demonstrate that all sprites MUST be in one
  single FRG to work correctly
- DirtySprite._layer is now READ only (using an _ now)
- DirtySprite.visible is a property now (so you do not habe to worry to set
  the sprite dirty when changing the visibility state

11.06.07: (v1.1.72)
- unittest for LayeredRenderGroup added

09.06.07: (v1.1.72)
- doc strings
- removed old FRG
- changed to v1.1

07.06.07: (v1.0.70)
- separated LayeredRenderGroup from the FRG
- LayeredRenderGroup extended with new methods

06.06.07: (v1.0.70)
- changed layersystem, sprite does not know anything about layers
- only through change_layer the layer of a sprite can be changed

04.06.07:
- fix change_layer to prevent infinit loop
- fix need of a view attribute for the sprite when adding it to a group in
  the __init__ method directly

03.06.07:
- fix: now you can create a group befor the display is initialized again
- fix: #223 changed . by _

03.06.07:
- proper version information and license information added

02.06.07:
- using background now
- verion() method added so you can get the version
- dirty flag defaults to 2 (old sprites as DirtySprite as well)
- default layer is set to ??

29.05.07:
- fixed clipping, works correctly now

"""

RELEASE = 1
SUBRELEASE = 1
REV = "$Rev: 93 $"
REV = REV[6:-1]

VERSION = 'FastRenderGroup v'+str(RELEASE)+'.'+str(SUBRELEASE)+'.'+REV+\
                                                        "  DR0ID (c) 2007"
VERSION_NUMBER = RELEASE, SUBRELEASE, int(REV)

del RELEASE
del SUBRELEASE
del REV

__author__ = "$Author: DR0ID $"
__version__ = VERSION
__date__ = "$Date: 2007-08-04 11:45:06 +0200 (Sa, 04 Aug 2007) $"
__license__ = 'LGPL, you should have received a copy as LGPL.txt'
__copyright__ = "DR0ID (c) 2007"
__url__ = "http://www.mypage.bluewin.ch/DR0ID/index.html"
__email__ = "dr0id@bluewin.ch"


import pygame
from pygame import Rect
from pygame.sprite import Sprite
from pygame.time import get_ticks




class DirtySprite(pygame.sprite.Sprite):
    """
    DirtySprite has new attributes:
    
    dirty: if set to 1, it is repainted and then set to 0 again 
           if set to 2 then it is always dirty ( repainted each frame)
           0 means that it is not dirty and therefor not repainted again
    blendmode: (for pygame 1.8) not used at the moment (actually its the 
                special_flags argument of blit)
    visible: normally 1, if set to 0 it will not be repainted 
             (you must set it dirty too to be erased from screen)
    """
    
    def __init__(self, *groups):
        """
        Same as pygame.sprite.Sprite but initializes the new attributes to
        default values:
        dirty = 1 (to be always dirty you have to set it)
        blendmode = 0
        layer = 0 (READONLY value, it is read when adding it to the 
                   LayeredRenderGroup, for details see doc of 
                   LayeredRenderGroup)
        """
        self.dirty = 1
        self.blendmode = 0  # pygame 1.8, reffered as special_flags in 
                            # the documentation of blit 
        self._visible = 1
        self._layer = 0    # READ ONLY by LayeredUpdates or LayeredDirty
        self.source_rect = None
        pygame.sprite.Sprite.__init__(self, *groups)
        
    def _set_visible(self, val):
        """set the visible value (0 or 1) and makes the sprite dirty"""
        self._visible = val
        if self.dirty < 2:
            self.dirty = 1
    def _get_visible(self):
        """returns the visible value of that sprite"""
        return self._visible
    visible = property(lambda self: self._get_visible(),\
                       lambda self, value:self._set_visible(value), \
                       doc="you can make this sprite disappear without removing it from the group, values 0 for invisible and 1 for visible")
        
        

class LayeredUpdates(pygame.sprite.AbstractGroup):
    """
    LayeredRenderGroup
    
    A group that handles layers. For drawing it uses the same metod as the 
    pygame.sprite.OrderedUpdates.
    
    This group is fully compatible with pygame.sprite.Sprite.
    """
    
    def __init__(self, *sprites, **kwargs):
        """
        You can set the default layer through kwargs using 'default_layer'
        and an integer for the layer. The default layer is 0.
        
        If the sprite you add has an attribute layer then that layer will
        be used.
        If the kwarg contain 'layer' then the sprites passed will be 
        added to that layer (overriding the sprite.layer attribute).
        If neither sprite has attribute layer nor kwarg then the default
        layer is used to add the sprites.
        """
        self._spritelayers = {}
        self._spritelist = []
        pygame.sprite.AbstractGroup.__init__(self)
        if kwargs.get('default_layer'):
            self._default_layer = kwargs['default_layer']
        else:
            self._default_layer = 0
            
        self.add(*sprites, **kwargs)
    
    def add_internal(self, sprite, layer=None):
        """
        Do not use this method directly. It is used by the group to add a
        sprite internally.
        """
        self.spritedict[sprite] = Rect(0, 0, 0, 0) # add a old rect
        
        if layer is None:
            if hasattr(sprite, '_layer'):
                layer = sprite._layer
            else:
                layer = self._default_layer
                
                
        self._spritelayers[sprite] = layer
        if hasattr(sprite, '_layer'):
            sprite._layer = layer
    
        # add the sprite at the right position
        # bisect algorithmus
        sprites = self._spritelist # speedup
        sprites_layers = self._spritelayers
        leng = len(sprites)
        low = 0
        high = leng-1
        mid = low
        while(low<=high):
            mid = low + (high-low)/2
            if(sprites_layers[sprites[int(mid)]]<=layer):
                low = mid+1
            else:
                high = mid-1
        # linear search to find final position
        while(mid<leng and sprites_layers[sprites[int(mid)]]<=layer):
            mid += 1
        sprites.insert(int(mid), sprite)
        
    def add(self, *sprites, **kwargs):
        """add(sprite, list, or group, ...)
           add sprite to group

           Add a sprite or sequence of sprites to a group.
        
        If the sprite(s) have an attribute layer then that is used 
        for the layer. If kwargs contains 'layer' then the sprite(s) 
        will be added to that argument (overriding the sprite layer 
        attribute). If neither is passed then the sprite(s) will be
        added to the default layer.
        """
        layer = None
        if kwargs.get('layer'):
            layer = kwargs['layer']
        if sprites is None or len(sprites)==0:
            return
        for sprite in sprites:
            # It's possible that some sprite is also an iterator.
            # If this is the case, we should add the sprite itself,
            # and not the objects it iterates over.
            if isinstance(sprite, Sprite):
                if not self.has_internal(sprite):
                    self.add_internal(sprite, layer)
                    sprite.add_internal(self)
            else:
                try:
                    # See if sprite is an iterator, like a list or sprite
                    # group.
                    for spr in sprite:
                        self.add(spr, **kwargs)
                except (TypeError, AttributeError):
                    # Not iterable, this is probably a sprite that happens
                    # to not subclass Sprite. Alternately, it could be an
                    # old-style sprite group.
                    if hasattr(sprite, '_spritegroup'):
                        for spr in sprite.sprites():
                            if not self.has_internal(spr):
                                self.add_internal(spr, layer)
                                spr.add_internal(self)
                    elif not self.has_internal(sprite):
                        self.add_internal(sprite, layer)
                        sprite.add_internal(self)
    
    def remove_internal(self, sprite):
        """
        Do not use this method directly. It is used by the group to 
        add a sprite.
        """
        self._spritelist.remove(sprite)
        # these dirty rects are suboptimal for one frame
        self.lostsprites.append(self.spritedict[sprite]) # dirty rect
        if hasattr(sprite, 'rect'):
            self.lostsprites.append(sprite.rect) # dirty rect
        
        self.spritedict.pop(sprite, 0)
        self._spritelayers.pop(sprite)
    
    def sprites(self):
        """
        Returns a ordered list of sprites (first back, last top).
        """
        return list(self._spritelist)
    
    def draw(self, surface):
        """
        Draw all sprites in the right order onto the passed surface.
        """
        spritedict = self.spritedict
        surface_blit = surface.blit
        dirty = self.lostsprites
        self.lostsprites = []
        dirty_append = dirty.append
        for spr in self.sprites():
            rec = spritedict[spr]
            newrect = surface_blit(spr.image, spr.rect)
            if rec is 0:
                dirty_append(newrect)
            else:
                if newrect.colliderect(rec):
                    dirty_append(newrect.union(rec))
                else:
                    dirty_append(newrect)
                    dirty_append(rec)
            spritedict[spr] = newrect
        return dirty

    def get_sprites_at(self, pos):
        """
        Returns a list with all sprites at that position.
        Bottom sprites first, top last.
        """
        _sprites = self._spritelist
        rect = Rect(pos, (0, 0))
        colliding_idx = rect.collidelistall(_sprites)
        colliding = []
        colliding_append = colliding.append
        for i in colliding_idx:
            colliding_append(_sprites[i])
        return colliding

    def get_sprite(self, idx):
        """
        Returns the sprite at the index idx from the sprites().
        Raises IndexOutOfBounds.
        """
        return self._spritelist[idx]
    
    def remove_sprites_of_layer(self, layer_nr):
        """
        Removes all sprites from a layer and returns them as a list.
        """
        sprites = self.get_sprites_from_layer(layer_nr)
        self.remove(sprites)
        return sprites
        

    #---# layer methods
    def layers(self):
        """
        Returns a list of layers defined (unique), sorted from botton up.
        """
        layers = set()
        for layer in self._spritelayers.values():
            layers.add(layer)
        return list(layers)

    def change_layer(self, sprite, new_layer):
        """
        Changes the layer of the sprite.
        sprite must have been added to the renderer. It is not checked.
        """
        sprites = self._spritelist # speedup
        sprites_layers = self._spritelayers # speedup
        
        sprites.remove(sprite) 
        sprites_layers.pop(sprite)
        
        # add the sprite at the right position
        # bisect algorithmus
        leng = len(sprites)
        low = 0
        high = leng-1
        mid = low
        while(low<=high):
            mid = low + (high-low)/2
            if(sprites_layers[sprites[mid]]<=new_layer):
                low = mid+1
            else:
                high = mid-1
        # linear search to find final position
        while(mid<leng and sprites_layers[sprites[mid]]<=new_layer):
            mid += 1
        sprites.insert(mid, sprite)
        if hasattr(sprite, 'layer'):
            sprite.layer = new_layer
        
        # add layer info
        sprites_layers[sprite] = new_layer
            
    def get_layer_of_sprite(self, sprite):
        """
        Returns the layer that sprite is currently in. If the sprite is not 
        found then it will return the default layer.
        """
        return self._spritelayers.get(sprite, self._default_layer)
    
    def get_top_layer(self):
        """
        Returns the number of the top layer.
        """
        return self._spritelayers[self._spritelist[-1]]
####        return max(self._spritelayers.values())
    
    def get_bottom_layer(self):
        """
        Returns the number of the bottom layer.
        """
        return self._spritelayers[self._spritelist[0]]
####        return min(self._spritelayers.values())
    
    def move_to_front(self, sprite):
        """
        Brings the sprite to front, changing the layer o the sprite
        to be in the topmost layer (added at the end of that layer).
        """
        self.change_layer(sprite, self.get_top_layer())
        
    def move_to_back(self, sprite):
        """
        Moves the sprite to the bottom layer, moving it behind
        all other layers and adding one additional layer.
        """
        self.change_layer(sprite, self.get_bottom_layer()-1)
        
    def get_top_sprite(self):
        """
        Returns the topmost sprite.
        """
        return self._spritelist[-1]
    
    def get_sprites_from_layer(self, layer):
        """
        Returns all sprites from a layer, ordered by how they where added.
        It uses linear search and the sprites are not removed from layer.
        """
        sprites = []
        sprites_append = sprites.append
        sprite_layers = self._spritelayers
        for spr in self._spritelist:
            if sprite_layers[spr] == layer: 
                sprites_append(spr)
            elif sprite_layers[spr]>layer:# break after because no other will 
                                          # follow with same layer
                break
        return sprites
        
    def switch_layer(self, layer1_nr, layer2_nr):
        """
        Switches the sprites from layer1 to layer2.
        The layers number must exist, it is not checked.
        """
        sprites1 = self.remove_sprites_of_layer(layer1_nr)
        for spr in self.get_sprites_from_layer(layer2_nr):
            self.change_layer(spr, layer1_nr)
        self.add(sprites1, layer=layer2_nr)


class LayeredDirty(LayeredUpdates):
    """
    Yet another group. It uses the dirty flag technique and is therefore 
    faster than the pygame.sprite.RenderUpdates if you have many static 
    sprites. It also switches automatically between dirty rect upte and 
    full screen rawing, so you do no have to worry what would be faster. It 
    only works with the DirtySprite or any sprite that has the following 
    attributes: image, rect, dirty, visible, blendmode (see doc of 
    DirtySprite).
    """
    
    def __init__(self, *sprites, **kwargs):
        """
        Same as for the pygame.sprite.Group.
        You can specify some additional attributes through kwargs:
        _use_update: True/False   default is False
        _default_layer: the default layer where the sprites without a layer are
                        added.
        _time_threshold: treshold time for switching between dirty rect mode and
                        fullscreen mode, defaults to 1000./80  == 1000./fps
        """
        LayeredUpdates.__init__(self, *sprites, **kwargs)
        self._clip = None
        
        self._use_update = False
        
        self._time_threshold = 1000./20. # 1000./ fps
        
        
        self._bgd = None
        for key, val in kwargs.items():
            if key in ['_use_update', '_time_threshold', '_default_layer']:
                if hasattr(self, key):
                    setattr(self, key, val)

    def add_internal(self, sprite, layer=None):
        """
        Do not use this method directly. It is used by the group to add a
        sprite internally.
        """
        # check if all attributes needed are set
        if not hasattr(sprite, 'dirty'):
            raise AttributeError()
        if not hasattr(sprite, "visible"):
            raise AttributeError()
        if not hasattr(sprite, "blendmode"):
            raise AttributeError()
        
        if not isinstance(sprite, DirtySprite):
            raise TypeError()
        
        if sprite.dirty == 0: # set it dirty if it is not
            sprite.dirty = 1
        
        LayeredUpdates.add_internal(self, sprite, layer)
        
    def draw(self, surface, bgd=None):
        """
        Draws all sprites on the surface you pass in.
        You can pass the background too. If a background is already set, 
        then the bgd argument has no effect.
        """
        # speedups
        _orig_clip = surface.get_clip()
        _clip = self._clip
        if _clip is None:
            _clip = _orig_clip
        
        
        _surf = surface
        _sprites = self._spritelist
        _old_rect = self.spritedict
        _update = self.lostsprites
        _update_append = _update.append
        _ret = None
        _surf_blit = _surf.blit
        _rect = pygame.Rect
        if bgd is not None:
            self._bgd = bgd
        _bgd = self._bgd
        
        _surf.set_clip(_clip)
        # -------
        # 0. deside if normal render of flip
        start_time = get_ticks()
        if self._use_update: # dirty rects mode
            # 1. find dirty area on screen and put the rects into _update
            # still not happy with that part
            for spr in _sprites:
                if 0 < spr.dirty:
                    if spr.source_rect is not None:
                        _union_rect = Rect(spr.rect.topleft, spr.source_rect.size)
                    else:
                        _union_rect = _rect(spr.rect)
                    _union_rect_collidelist = _union_rect.collidelist
                    _union_rect_union_ip = _union_rect.union_ip
                    i = _union_rect_collidelist(_update)
                    while -1 < i:
                        _union_rect_union_ip(_update[i])
                        del _update[i]
                        i = _union_rect_collidelist(_update)
                    _update_append(_union_rect.clip(_clip))
                    
                    _union_rect = _rect(_old_rect[spr])
                    _union_rect_collidelist = _union_rect.collidelist
                    _union_rect_union_ip = _union_rect.union_ip
                    i = _union_rect_collidelist(_update)
                    while -1 < i:
                        _union_rect_union_ip(_update[i])
                        del _update[i]
                        i = _union_rect_collidelist(_update)
                    _update_append(_union_rect.clip(_clip))
            # can it be done better? because that is an O(n**2) algorithm in
            # worst case
                    
            # clear using background
            if _bgd is not None:
                for rec in _update:
                    _surf_blit(_bgd, rec, rec)
                
            # 2. draw
            for spr in _sprites:
                if 1 > spr.dirty:
                    if spr._visible:
                        # sprite not dirty, blit only the intersecting part
                        if spr.source_rect is not None:
                            _spr_rect = Rect(spr.rect.topleft, spr.source_rect.size)
                        else:
                            _spr_rect = spr.rect
                        _spr_rect_clip = _spr_rect.clip
                        for idx in _spr_rect.collidelistall(_update):
                            # clip
                            clip = _spr_rect_clip(_update[idx])
                            _surf_blit(spr.image, clip, \
                                       (clip[0]-_spr_rect[0], \
                                            clip[1]-_spr_rect[1], \
                                            clip[2], \
                                            clip[3]))#, spr.blendmode)
                else: # dirty sprite
                    if spr._visible:
                        if spr.source_rect is not None:
                            _old_rect[spr] = _surf_blit(spr.image, spr.rect, \
                                               spr.source_rect)#, spr.blendmode)
                        else:
                            _old_rect[spr] = _surf_blit(spr.image, spr.rect)

                    if spr.dirty == 1:
                        spr.dirty = 0
            _ret = list(_update)
        else: # flip, full screen mode
            if _bgd is not None:
                _surf_blit(_bgd, (0, 0))
            for spr in _sprites:
                if spr.visible:
                    if spr.source_rect is not None:
                        _old_rect[spr] = _surf_blit(spr.image, spr.rect, spr.source_rect)#,spr.blendmode)
                    else:
                        _old_rect[spr] = _surf_blit(spr.image, spr.rect)#, spr.source_rect)#,spr.blendmode)
            _ret = [_rect(_clip)] # return only the part of the screen changed
            
        
        # timing for switching modes
        # how to find a good treshold? it depends on the hardware it runs on
        end_time = get_ticks()
        if end_time-start_time > self._time_threshold:
            self._use_update = False
        else:
            self._use_update = True
            
##        # debug
##        print "               check: using dirty rects:", self._use_update
            
        # emtpy dirty reas list
        _update[:] = []
        
        # -------
        # restore original clip
        _surf.set_clip(_orig_clip)
        return _ret

    def clear(self, surface, bgd):
        """
        Only used to set background.
        """
        self._bgd = bgd

    def repaint_rect(self, screen_rect): 
        """
        Repaints the given area.
        screen_rect in screencoordinates.
        """
        self.lostsprites.append(screen_rect.clip(self._clip))
        
    def set_clip(self, screen_rect=None):
        """
        clip the area where to draw. Just pass None (default) to 
        reset the clip.
        """
        if screen_rect is None:
            self._clip = pygame.display.get_surface().get_rect()
        else:
            self._clip = screen_rect
        self._use_update = False
        
    def get_clip(self):
        """
        Returns the current clip.
        """
        return self._clip
    
    def change_layer(self, sprite, new_layer):
        """
        Changes the layer of the sprite.
        sprite must have been added to the renderer. It is not checked.
        """
        LayeredRenderGroup.change_layer(self, sprite, new_layer)
        if sprite.dirty == 0:
            sprite.dirty = 1
            
    def set_timing_treshold(self, time_ms):
        """
        Sets the treshold in milliseconds. Default is 1000./80 where 80 is the
        fps I want to switch to full screen mode.
        """
        self._time_threshold = time_ms
    


