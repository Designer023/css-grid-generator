from __future__ import division
import math

#VERSION 01
#TODO: Padding in and out of grid and sub grid
#TODO: FIX FOR PERCENTAGE BUGS if possible

def generate_grid(prefix, fullGridColumns, gridWrapperWidth, gutterWidthInPX, filename=None):
	#------------ GRID PROPERTIES -----------------#
	

	#Gutters
	gutters = fullGridColumns - 1
	gutterPercentage = gutterWidthInPX/gridWrapperWidth*100
	#Columns
	columnSpace = gridWrapperWidth - (gutters * gutterWidthInPX)
	columnWidth = columnSpace / fullGridColumns;
	column_width_percentage = (columnWidth / gridWrapperWidth * 100)
	
	#------------ CREATE SELECTORS AND PROPS -----------------#

	
	if fullGridColumns > 1:
		#mutliple columns

		#------------ Work out the selectors properties -----------------#
		
		ouputString = ''
		
		#/* Grid grid: 8 column / gutter: 2.02020202% ---------------------------------------- */
		classStr = ''
		for w in range (1, fullGridColumns+ 1):#loop all the ranges from 1 - cols
			classStr += '[class*=%s%s],' %(prefix, w)
		
		classStr += '.%s-all'%(prefix)
		cssProperty = '{display:block;float:left;margin-right:%f%%;margin-left:0;}\n\n' %(gutterPercentage)
		classStr = classStr.rstrip(",")
		classStr += cssProperty
		ouputString += classStr
		
		#WIDTHS
		#.XDn

		classStr = ''
		for w in range (1, fullGridColumns+ 1):
			classStr += '.%s%s,' %(prefix, w)
		
		cssProperty = '{width:%f%%;}' %(column_width_percentage)
		classStr = classStr.rstrip(",")
		classStr += cssProperty
		ouputString += classStr


		
		for width in range (1, fullGridColumns):
			classStr = ''
			for idx in range (1, fullGridColumns- width + 1):
				for childIXD in range (idx, idx+width + 1):
					classStr += '.%s%i-%s%i .%s%i,' %(prefix, idx, prefix, idx+width, prefix, childIXD)
			#MATH
			parentColumnWidthinPX = columnWidth + ((width) * (gutterWidthInPX + columnWidth))
			childColumnWidthinPX = columnWidth
			colWidth = childColumnWidthinPX / parentColumnWidthinPX * 100
						
			#output
			classStr = classStr.rstrip(",")
			cssProperty = '{width:%f%%;}' %(colWidth)
			classStr += cssProperty
			ouputString += classStr
		


		for additionalCols in range(1, fullGridColumns - 1):
			#/* #{$additionalCols} spans */
			classStr = ''
			for startIDX in range(1, fullGridColumns - additionalCols + 1):
				classStr += '.%s%i-%s%i,' %(prefix, startIDX, prefix, startIDX + additionalCols)
				
			#MATHS
			parentWidthInPX = gridWrapperWidth

			missingMarginWidth = columnWidth + ((additionalCols) * (gutterWidthInPX + columnWidth))
			
			column_width_percentage = missingMarginWidth / parentWidthInPX * 100
			#output css
			cssProperty = '{width:%f%%;}' %(column_width_percentage)
			classStr = classStr.rstrip(",")
			classStr += cssProperty
			ouputString += classStr


		for childWidth in range (1, fullGridColumns):
			for parentWidth in range (2, fullGridColumns):
				if childWidth < parentWidth:
					#/* sub widths for #{$parentWidth} spans - #{childWidth} sub elements */
					classStr = ''
					for parentSelector in range (1 , fullGridColumns):
						if (parentSelector + parentWidth) <= fullGridColumns:


							for childSelector in range (parentSelector, (parentSelector + parentWidth)):
								if (childSelector + childWidth) <= (parentSelector + parentWidth):
									classStr += '.%s%i-%s%i .%s%i-%s%i,' %(prefix, parentSelector, prefix, (parentSelector + parentWidth), prefix, childSelector, prefix, (childSelector + childWidth))
									
									
					parentColumnWidthinPX = columnWidth + (parentWidth * (gutterWidthInPX + columnWidth))
					childColumnWidthinPX = columnWidth + (childWidth * (gutterWidthInPX + columnWidth))

					

					colWidth = childColumnWidthinPX / parentColumnWidthinPX * 100
					cssProperty = '{width:%f%%;}' %(colWidth)
					classStr = classStr.rstrip(",")
					if classStr != '' :
						classStr += cssProperty
						ouputString += classStr
		
		
		classStr += '.%s-all'%(prefix)
		cssProperty = '{width:100%;margin-left:0;margin-right:0;}'
		classStr = classStr.rstrip(",")
		classStr += cssProperty
		ouputString += classStr

		ouputString += '\n\n'

		#/* Grid grid margins and clearing ----- */
		ouputString += '\n\n/* Grid grid margins and clearing ----- */\n'
		

		for parentSpans in range(1,fullGridColumns-1):
			classStr = ''
			for parentIDX in range(1, fullGridColumns - parentSpans + 1):
				for idx in range(parentIDX, parentIDX + parentSpans + 1):
					if idx != parentIDX:
						for subIdx in range (idx, parentIDX + parentSpans):
							classStr += '.%s%i-%s%i [class*=%s%i],' %(prefix, parentIDX, prefix, parentIDX + parentSpans, prefix, subIdx)	
					
					classStr += '.%s%i-%s%i .%s%i,' %(prefix, parentIDX, prefix, parentIDX + parentSpans, prefix, idx)

			#WIDTH MATHS
			parentColumnWidthinPX = columnWidth + (parentSpans * (gutterWidthInPX + columnWidth))
			gutterWidth = gutterWidthInPX / parentColumnWidthinPX * 100
			
			cssProperty = '{margin-right:%f%%;}' %(gutterWidth)
			classStr = classStr.rstrip(",")
			classStr += cssProperty
			ouputString += classStr






		ouputString += '\n\n/* Grid grid margins on right are 0 ----- */\n'

		classStr = ''
		for parentWidth in range (2, fullGridColumns + 1):
			classStr += '[class*=-%s%i] .%s%i,' %(prefix, parentWidth, prefix, parentWidth)
			classStr += '[class*=-%s%i] [class*=-%s%i],' %(prefix, parentWidth, prefix, parentWidth)


		classStr += '[class*=-%s%i],' %(prefix, fullGridColumns)
		classStr += '.%s%i' %(prefix, fullGridColumns)

		classStr = classStr.rstrip(",")
		cssProperty = '{margin-right:0;}'
		classStr += cssProperty
		ouputString += classStr	

	




		

		#/* Grid grid padding ----- */
		
		#/* ---------------------------- TO DO... Later if needed


		#/* Grid grid relationships ----- */
		
		ouputString += '\n\n/* Grid grid relationships ----- */\n'




		for missingRows in range(1, fullGridColumns):
			classStr = ''
			#if missingRows != 1:
			classStr += ".%s%i," %(prefix, missingRows + 1)
			if missingRows < (fullGridColumns ):
				classStr += "[class*=%s%i-]," %(prefix, missingRows + 1)	
			
			
			for val in range (missingRows + 1, fullGridColumns):
				
				lastNumber = val - (missingRows + 1)
				if lastNumber > 0:
					classStr += '.%s%i+.%s%i,' %(prefix, lastNumber, prefix, val)
					classStr += '.%s%i+[class*=%s%i-],' %(prefix, lastNumber, prefix, val)
					classStr += '[class*=-%s%i] + .%s%i,' %(prefix, lastNumber, prefix, val)
					classStr += '[class*=-%s%i] + [class*=%s%i-],' %(prefix, lastNumber, prefix, val)
			
		
			#WIDTH MATHS
			
			gapPX = (columnWidth + gutterWidthInPX )* (missingRows)
			gapPercent = gapPX /  gridWrapperWidth * 100
			#output css
			cssProperty = '{margin-left:%f%%;}' %(gapPercent)
			classStr = classStr.rstrip(",")
			classStr += cssProperty
			ouputString += classStr
	
		
		#/ sub grid relationship */
		ouputString += '\n\n/* sub grid relationship ----- */\n'
		for parentWidth in range (1, fullGridColumns):
			for spareMargins in range (1, parentWidth):
				classStr = ''
				for parentIDX in range (1, fullGridColumns - parentWidth + 1):
					
					for childIDX in range (parentIDX, parentIDX+ parentWidth + 1):
						if childIDX == parentIDX + spareMargins - 1:
							#on items with !width! index gap to left but no preceding item
							classStr += '.%s%i-%s%i .%s%i,'%(prefix, parentIDX, prefix, parentIDX+ parentWidth, prefix, childIDX)
							classStr += '.%s%i-%s%i [class*=%s%i-],'%(prefix, parentIDX, prefix, parentIDX+ parentWidth, prefix, childIDX)
							classStr += '.%s%i-%s%i [class*=%s%i-][class*=%s%i-].%s-clear,'%(prefix, parentIDX, prefix, parentIDX+ parentWidth, prefix, childIDX, prefix, childIDX, prefix)
							classStr += '.%s%i-%s%i .%s%i.%s%i.%s-clear,'%(prefix, parentIDX, prefix, parentIDX+ parentWidth, prefix, childIDX, prefix, childIDX, prefix)

						
						if spareMargins + childIDX < parentIDX + parentWidth + 1:
							#if the does not contains the last item in the column
							classStr += '.%s%i-%s%i .%s%i+.%s%i,'%(prefix, parentIDX, prefix, parentIDX+ parentWidth, prefix, childIDX, prefix, childIDX + spareMargins)
							if spareMargins + childIDX > parentIDX + spareMargins:
								classStr += '.%s%i-%s%i [class*=-%s%i]+.%s%i,'%(prefix, parentIDX, prefix, parentIDX+ parentWidth, prefix, childIDX, prefix, childIDX + spareMargins)

						if spareMargins + childIDX < parentIDX+ parentWidth:
							classStr += '.%s%i-%s%i [class*=-%s%i]+[class*=%s%i-],'%(prefix, parentIDX, prefix, parentIDX+ parentWidth, prefix, childIDX, prefix, childIDX + spareMargins)
							classStr += '.%s%i-%s%i .%s%i+[class*=%s%i-],'%(prefix, parentIDX, prefix, parentIDX+ parentWidth, prefix, childIDX, prefix, childIDX + spareMargins)

				#WIDTH MATHS
				parentColumnWidthinPX = columnWidth + ((parentWidth) * (gutterWidthInPX + columnWidth))
				gapWidth = (spareMargins - 1) * (gutterWidthInPX + columnWidth)
				gapPercent = gapWidth/parentColumnWidthinPX * 100
				#output css
				if gapPercent != 0:
					classStr = classStr.rstrip(",")
					cssProperty = '{margin-left:%f%%;}' %(gapPercent)
					classStr += cssProperty
					ouputString += classStr







		ouputString += '\n\n/* Grid first items margin left is 0 ----- */\n'

		classStr=''
		for idx in range (1, fullGridColumns + 1):
			classStr+='[class*=%s%i-] [class*=%s%i-],[class*=%s%i-] .%s%i,' %(prefix, idx, prefix, idx, prefix, idx, prefix, idx)
			classStr+='[class*=%s%i]+[class*=%s%i],' %(prefix, idx, prefix, idx+1)
			
			

		#output css
		classStr = classStr.rstrip(",")
		cssProperty = '{margin-left:0;}'
		classStr += cssProperty
		ouputString += classStr





		ouputString += '\n\n.%s1,[class*=%s1-],.%s-all,.%s-clear{clear:left;}' %(prefix, prefix, prefix, prefix)
		#/* Grid hiding ----- */
		ouputString += '\n\n/* Grid hiding ----- */\n'
		ouputString += '.%s-hide{display:none !important;}' %prefix
		






		#-------------WRITE FILE -------------------#
		#open file/create file
		try:
		    css=open(filename+'.css', 'w')
		except TypeError:
		    css=open(prefix+".css", 'w')
		
		css.write(ouputString)
		
		css.close()
	


if __name__ == '__main__':
    generate_grid("g", 8, 990, 20)