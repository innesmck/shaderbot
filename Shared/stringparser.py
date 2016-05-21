import sys, random

class Parser:
	# comment
	def __init__( self, grammar ):
		self.grammar = grammar

	def ChoosePhrase( self, phrases ):
		output = random.choice( phrases )
		return output
	
	def Parse( self, root ):
		output = self.ChoosePhrase( self.grammar[ root ] )

		while output.find( '$' ) != -1:
			first = output.find( '$' )
			last  = output.find( '$', first + 1 )
			split = output.find( ':', first + 1, last )

			raw  = output[first:last+1]
			token = output[first+1:last]

			if split != -1:
				token = output[first+1:split]

			replacement = ""
			if isinstance( self.grammar[ token ], dict ):
				replacement = self.ChoosePhrase( self.grammar[ token ][ "vals" ] )
				i = 0
				split1 = split + 1
				split2 = output.find( ':', split1, last )
				while self.grammar[ token ].has_key( "param" + str(i) ):
					if split2 == -1:
						split2 = last
					var    = output[split1:split2]
					replacement = replacement.replace( self.grammar[ token ][ "param" + str(i) ], var )
					i += 1
					split1 = split2 + 1
					split2 = output.find( ':', split1 + 1, last )

			else:
				replacement = self.ChoosePhrase( self.grammar[ token ] )

			output = output.replace( raw, replacement, 1 )
		return output

