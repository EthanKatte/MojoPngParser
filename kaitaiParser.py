import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from png import Png
import pprint

def get_png(filename):
    with open(filename, 'rb') as f:
        png_file = Png(KaitaiStream(BytesIO(f.read())))
    return png_file

def var_object(obj, initial_type=None):
    return vars(obj)

def unwrap_object(obj, prev=[]):
    prev.append(obj)
    attributes = var_object(obj)
    for key in attributes.keys():
        if isinstance(attributes[key], bytes) and len(attributes[key]) > 20:
            #big chunks of binary data is ignored
            attributes[key] = "BINARY DATA"
        
        if attributes[key] not in prev:
            if isinstance(attributes[key], list):
                elements = []
                for ele in attributes[key]:
                    elements.append(unwrap_object(ele))
                attributes[key] = elements 
            elif isinstance(attributes[key], Png.IhdrChunk) :
                attributes[key] = unwrap_object(attributes[key], prev)
            elif isinstance(attributes[key], Png.Chunk):
                attributes[key] = unwrap_object(attributes[key], prev)
            elif isinstance(attributes[key], Png.GamaChunk):
                attributes[key] = unwrap_object(attributes[key], prev)
            elif isinstance(attributes[key], Png.TextChunk):
                attributes[key] = unwrap_object(attributes[key], prev)
            elif isinstance(attributes[key], Png.TimeChunk):
                attributes[key] = unwrap_object(attributes[key], prev)
            elif isinstance(attributes[key], Png.PhysChunk):
                attributes[key] = unwrap_object(attributes[key], prev)
        
    return attributes
#un commenting this and running 'python kaitaiParser.py > testOutput.py' allows you to see the structure of the file 
#pprint.pprint(unwrap_object(get_png("./dinosaur.png")))

'''
{
 '_io': <kaitaistruct.KaitaiStream object at 0x7f7c380a3c40>,
 '_parent': None,
 '_root': <png.Png object at 0x7f7c28724df0>,
 'magic': b'\x89PNG\r\n\x1a\n',
 'ihdr_len': 13,
 'ihdr_type': b'IHDR',
 'ihdr': <png.Png.IhdrChunk object at 0x7f7c28766590>,
 'ihdr_crc': b'4\xa6y\x84',
 'chunks': [<png.Png.Chunk object at 0x7f7c287ee800>,
            <png.Png.Chunk object at 0x7f7c287ee980>,
            <png.Png.Chunk object at 0x7f7c287eead0>,
            <png.Png.Chunk object at 0x7f7c287eec50>,
            <png.Png.Chunk object at 0x7f7c287eee60>,
            <png.Png.Chunk object at 0x7f7c287eeef0>,
            <png.Png.Chunk object at 0x7f7c287eef50>,
            <png.Png.Chunk object at 0x7f7c287eefb0>,
            <png.Png.Chunk object at 0x7f7c287ef010>,
            <png.Png.Chunk object at 0x7f7c287ef070>,
            <png.Png.Chunk object at 0x7f7c287ef0d0>,
            <png.Png.Chunk object at 0x7f7c287ef130>,
            <png.Png.Chunk object at 0x7f7c287ef190>,
            <png.Png.Chunk object at 0x7f7c287ef1f0>,
            <png.Png.Chunk object at 0x7f7c287ef250>,
            <png.Png.Chunk object at 0x7f7c287ef2b0>,
            <png.Png.Chunk object at 0x7f7c287ef310>,
            <png.Png.Chunk object at 0x7f7c287ef370>,
            <png.Png.Chunk object at 0x7f7c287ef3d0>,
            <png.Png.Chunk object at 0x7f7c287ef430>,
            <png.Png.Chunk object at 0x7f7c287ef490>,
            <png.Png.Chunk object at 0x7f7c287ef4f0>,
            <png.Png.Chunk object at 0x7f7c287ef550>,
            <png.Png.Chunk object at 0x7f7c287ef5b0>,
            <png.Png.Chunk object at 0x7f7c287ef610>,
            <png.Png.Chunk object at 0x7f7c287ef670>,
            <png.Png.Chunk object at 0x7f7c287ef6d0>,
            <png.Png.Chunk object at 0x7f7c287ef730>,
            <png.Png.Chunk object at 0x7f7c287ef790>,
            <png.Png.Chunk object at 0x7f7c287ef7f0>]
}




'''