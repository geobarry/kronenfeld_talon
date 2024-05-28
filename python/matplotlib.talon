tag: user.my_python
-
import matplotlib: insert("import matplotlib.pyplot as plt")
import matplotlib patches: insert("import matplotlib.patches as mpatches")
import matplotlib path: insert("import matplotlib.path as mpath\nPath = mpath.Path")
[matplotlib] create subplots: user.insert_between("fig, axes = plt.subplots(",")")
[matplotlib] show plot: insert("plt.show()")
	
# AXIS LABELS AND TICK MARKS
axis off: insert("ax.axis('off')")
axis equal: insert("ax.axis('equal')")
set axis title: user.insert_between("ax.set_title('","', y = -0.3)")
{user.variable_list} dot plot: user.insert_between("{user.variable_list}.plot(",")")
{user.variable_list} dot text: user.insert_between("{user.variable_list}.text(",")")
plot axis equal: insert("plt.axis('equal')")
plot save figure: user.insert_between("plt.savefig(",")")

# EXPERIMENTAL
[matplotlib] create Bezier [curve]:
	insert("curve_def = (")
	key(enter:2 up)
	insert("[(0,0),Path.MOVETO],")
	key(enter)
	insert("[(10,0),Path.CURVE3],")
	key(enter)
	insert("[(10,10),Path.CURVE3]")
	key(down)
	key(enter)
	insert("v,paths = zip(*curve_def)")
	key(enter)
	insert("pp1 = mpatches.PathPatch(")
	key(enter:2)
	key(up)
	insert("Path(v,paths),")
	key(enter)
	insert('fc="none",')
	key(enter)
	insert("transform=ax.transData")
	key(down)
	key(enter)
	insert("ax.add_patch(pp1)")
	key(enter)
[matplotlib] insert Bezier vertex:
	edit.line_insert_down()
	user.insert_between("[(","),Path.CURVE3],")

