#!/usr/bin/env python
#-*- coding: utf8 -*-

import re
import collections
import codecs

def words( text ):
    return re.findall( '[a-ź]+', text.lower() )

def train( features ):
    model = collections.defaultdict( lambda: 1 )
    for f in features:
        model[f] += 1
    return model

class Corrector:
    alphabet = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
        'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
        'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
        'y', 'z', 'ź', 'ż', 'ó', 'ł', 'ś', 'ć',
        'ń', 'ę', 'ą' 
    ]

    def __init__( self, filename ):
        print " -- trwa tworzenie słownika ..."        
        self.dictionary = train( words( file( filename ).read() ) )

    def correct( self, file_in, file_out ):
        print " -- poprawa pisowni pliku %s => %s " % ( file_in, file_out )
        
        output = []
        errors = 0

        for word in re.compile( "(\W+)", re.U ).split( codecs.open( file_in, 'r', 'utf-8' ).read() ):
            
            word = word.encode( 'utf-8' )
            if re.match( "[a-źA-Ź]+", word ):
                word = word.lower()
                rep = word

                if not self.known( [ word ] ):
                    print "* BŁĄD W SŁOWIE: %s" % word

                    errors += 1

                    edits1 = self.known( self.get_edits( word ) )
                    edits2 = self.known( self.get_edits2( word ) )
                    
                    if len( edits1 ) + len( edits2 ) > 0:
                        counter = 1
                        tmp_dc = []

                        print " Lista proponowanych słów: " 
                        for el in edits1:
                            if counter == 50:
                                break
                            print "  %-2d --> %s" % ( counter, el )
                            tmp_dc.append( el )
                            counter += 1 

                        if len( edits1 ) > 0:
                            print " ------- "
                            for el in edits2:
                                if counter == 50:
                                    break
                                print "  %-2d --> %s" % ( counter, el )
                                tmp_dc.append( el )
                                counter += 1 

                        rep = self.get_input( tmp_dc, word )
                    else:
                        print " Brak propozycji ..."

                output.append( rep )

            else:
                output.append( word )
        
        file = codecs.open( file_out, "w", "utf-8" )
        file.write( unicode( ''.join( output ) ) )
        file.close()

        print " -- zakończono poprawę pliku. Liczba błędów: %d" % errors
        print "\n == Dziękuję, dobranoc ==\n"

    def get_input( self, elements, word ):
        x = None
        while x is None:
            print "Podaj numer elementu na który chcesz zamieńić podane słowo, 0 aby zignorować ten błąd: "
            try:
                x = int( raw_input() )
            except ValueError:
                pass

        if x == 0:
            return word

        try:
            return elements[x - 1]
        except IndexError:
            return self.get_input( elements, word )

    def known( self, words ):
        return set( w for w in words if w in self.dictionary )

    def get_edits( self, word ):
        splits     = [ ( word[:i], word[i:] ) for i in range( len( word ) + 1 ) ]
        deletes    = [ a + b[1:] for a, b in splits if b ]
        transposes = [ a + b[1] + b[0] + b[2:] for a, b in splits if len( b ) > 1 ]
        replaces   = [ a + c + b[1:] for a, b in splits for c in self.alphabet if b ]
        inserts    = [ a + c + b     for a, b in splits for c in self.alphabet ]
        return set( deletes + transposes + replaces + inserts )
    
    def get_edits2( self, word ):
        return set( e2 for e1 in self.get_edits( word ) for e2 in self.get_edits( e1 ) if e2 in self.dictionary )

if __name__ == "__main__":
    from sys import argv

    if len( argv ) is not 3:
        print "Usage: %s <PLIK_DO_SPRAWDZENIA_POPRAWNOŚCI> <POPRAWIONY_PLIK>" % argv[0]
        exit( -1 )

    print "\n == Program korekty tekstu ==\n"

    corrector = Corrector( 'formy.txt.utf8' )
    corrector.correct( argv[1], argv[2] )


# vim: ai fdm=marker ts=4 sw=4 sts=4
