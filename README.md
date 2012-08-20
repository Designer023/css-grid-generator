CSS-Grid-Generator
==================

A CSS Grid generator that uses SCSS or Python to generate a grid and sub-grid. Based on the logic that gridsetapp.com uses, only more rough. The grid is based on a flexible width with percentages. Multiple grids can be triggered by using @mediaqueries.

@include grid(gridname, columns, gridwidth, gutter);

Usage (SCSS):
    
    @import 'grid.scss';
		@include grid(g, 8, 990, 20);

This will create a grid with 8 columns with the prefix 'g' that spans 990px with 20px gutters between columns.

Styles can be applied to columns using:
    
    … class="g1-g4" …

This will apply a 4 column span to the column.

To-do:
------

-Specify each individual column width
-Option to produce fixed width grid with px values
