import java.io.BufferedReader;
import java.io.InputStreamReader;

import java.util.Iterator;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.LinkedList;
import java.util.Map;
import java.util.HashMap;

public class Potop {
	public static void main( String[] args ) throws Exception {
		Map<String, Integer> words = new HashMap<String, Integer>();

		BufferedReader in = new BufferedReader( new InputStreamReader( System.in ) );
		String line;
		while( ( line = in.readLine() ) != null ) {
			String[] lineSpl = line.toLowerCase().split( "[^a-ź]+" );
			for( String word: lineSpl )
				if( !word.isEmpty() )
					words.put( word, words.containsKey( word ) ? words.get( word ) + 1 : 1 );
		}

		List list = new LinkedList( words.entrySet() );
		Collections.sort( list, new Comparator() {
			@Override public int compare( Object o1, Object o2 ) {
				return ( (Comparable) ( (Map.Entry) o2 ).getValue() )
							.compareTo(
					    		( (Comparable) ( (Map.Entry) o1 ).getValue() )
							);
			}
		} );
		
		Iterator it = list.iterator();
		for( int i = 0; it.hasNext() && i < 20; i++ ) {
			Map.Entry entry = (Map.Entry) it.next();
			System.out.println( entry.getKey() + " " + entry.getValue() );
		}
	}
}
