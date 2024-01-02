---
type: rule
title: Do you know the difference between a 'smart' and a 'clever' developer?
uri: do-you-know-the-difference-between-a-clever-and-a-smart-developer
authors:
  - title: Andrew Harris
    url: https://www.ssw.com.au/people/andrew-harris
  - title: Jack Duan
    url: https://www.ssw.com.au/people/jack-duan
  - title: William Liebenberg
    url: https://www.ssw.com.au/people/william-liebenberg
created: 2022-09-23T01:44:15.693Z
guid: 57fd6a3d-7685-4f36-bb39-90b6af6c3565

---

When we first start out as a developer, we want to show the world what we can do by creating complex solutions. As we gain experience, we learn to show our worth by creating simple solutions.

> Developers are like a fine wine, they get better with age. 

<!--endintro-->

Lets take this piece of code as an example:

```html
<span className="text-xl">
    {
        targetedDays === 0 ? "Today" : 
        targetedDays === -1 ? "Yesterday" : 
        targetedDays === 1 ? "Tomorrow" : 
        moment().add(targetedDays, 'days').format("dddd D MMMM YYYY")
    }
</span>
```

One liner! Nailed it 🥳 Pity the next developer who has to decipher what is going on! The [cognitive load](https://en.wikipedia.org/wiki/Cognitive_load) here is really high! and the the maintainability, is really low. What is the first thing you are going to need to do if this piece of code start behaving poorly?

Now lets take the following reformatted code example:

```js
const getTargetedDayAsText = (targetedDays) => {
  if (targetedDays === -1) {
    return "Yesterday";
  } elseif (targetedDays === 0) {
    return "Today";
  } elseif (targetedDays === 1) {
    return "Tomorrow";
  } else {
    let days = moment().add(targetedDays, 'days');
    let formatted = days.format("dddd D MMMM YYYY");
    return formatted;
  }
}

<span className="text-xl">
    {getTargetedDayAsText(targetedDays)}
</span>
```

Now this is nowhere near as terse, but anyone looking at it is able to quickly determine what is going on. And anyone who has to investigate any issue with the code is going to be able to step through and debug this without any issues.

This above is not an overly complicated example but now imagine something like this [example](https://learn.microsoft.com/en-us/archive/blogs/lukeh/taking-linq-to-objects-to-extremes-a-fully-linqified-raytracer)

```js
var pixelsQuery =
    from y in Enumerable.Range(0, screenHeight)
    let recenterY = -(y - (screenHeight / 2.0)) / (2.0 * screenHeight)
    select from x in Enumerable.Range(0, screenWidth)
           let recenterX = (x - (screenWidth / 2.0)) / (2.0 * screenWidth)
           let point =
               Vector.Norm(Vector.Plus(scene.Camera.Forward,
                                       Vector.Plus(Vector.Times(recenterX, scene.Camera.Right),
                                                   Vector.Times(recenterY, scene.Camera.Up))))
           let ray = new Ray() { Start = scene.Camera.Pos, Dir = point }
           let computeTraceRay = (Func<Func<TraceRayArgs, Color>, Func<TraceRayArgs, Color>>)
            (f => traceRayArgs =>
             (from isect in
                  from thing in traceRayArgs.Scene.Things
                  select thing.Intersect(traceRayArgs.Ray)
              where isect != null
              orderby isect.Dist
              let d = isect.Ray.Dir
              let pos = Vector.Plus(Vector.Times(isect.Dist, isect.Ray.Dir), isect.Ray.Start)
              let normal = isect.Thing.Normal(pos)
              let reflectDir = Vector.Minus(d, Vector.Times(2 * Vector.Dot(normal, d), normal))
              let naturalColors =
                  from light in traceRayArgs.Scene.Lights
                  let ldis = Vector.Minus(light.Pos, pos)
                  let livec = Vector.Norm(ldis)
                  let testRay = new Ray() { Start = pos, Dir = livec }
                  let testIsects = from inter in
                                       from thing in traceRayArgs.Scene.Things
                                       select thing.Intersect(testRay)
                                   where inter != null
                                   orderby inter.Dist
                                   select inter
                  let testIsect = testIsects.FirstOrDefault()
                  let neatIsect = testIsect == null ? 0 : testIsect.Dist
                  let isInShadow = !((neatIsect > Vector.Mag(ldis)) || (neatIsect == 0))
                  where !isInShadow
                  let illum = Vector.Dot(livec, normal)
                  let lcolor = illum > 0 ? Color.Times(illum, light.Color) : Color.Make(0, 0, 0)
                  let specular = Vector.Dot(livec, Vector.Norm(reflectDir))
                  let scolor = specular > 0
                                 ? Color.Times(Math.Pow(specular, isect.Thing.Surface.Roughness),
                                               light.Color)
                                 : Color.Make(0, 0, 0)
                  select Color.Plus(Color.Times(isect.Thing.Surface.Diffuse(pos), lcolor),
                                    Color.Times(isect.Thing.Surface.Specular(pos), scolor))
              let reflectPos = Vector.Plus(pos, Vector.Times(.001, reflectDir))
              let reflectColor = traceRayArgs.Depth >= MaxDepth
                                  ? Color.Make(.5, .5, .5)
                                  : Color.Times(isect.Thing.Surface.Reflect(reflectPos),
                                                f(new TraceRayArgs(new Ray()
                                                {
                                                    Start = reflectPos,
                                                    Dir = reflectDir
                                                },
                                                                   traceRayArgs.Scene,
                                                                   traceRayArgs.Depth + 1)))
              select naturalColors.Aggregate(reflectColor,
                                             (color, natColor) => Color.Plus(color, natColor))
             ).DefaultIfEmpty(Color.Background).First())
           let traceRay = Y(computeTraceRay)
           select new { X = x, Y = y, Color = traceRay(new TraceRayArgs(ray, scene, 0)) };

foreach (var row in pixelsQuery)
    foreach (var pixel in row)
        setPixel(pixel.X, pixel.Y, pixel.Color.ToDrawingColor());
```

This was fortunately just someone's exercise in proving that they could and happily states 

> Just because you can, doesn't mean you should!

So what are some of the things that developers learn over time that takes them from being a Clever developer to being a Smart developer?

### Avoiding problems

Clever developers fix a problem where Smart Developers stop a problem from happening. 

Lets say you receive a PBI saying that XYZ method is always returning a value 0.001 more than it should. 

**Smart Developer**

Identifies that some incoming data is always out and results in the small rounding issue. 

```js
return (value-0.001) 
```

**Clever Developer**

Identifies that a method downstream is rounding to 2 decimal places and removes this. 

### Understanding the whole before they start

Code costs money, not just to create but also to maintain. 

![Figure: Clever developer coding away and resolving PBI's](https://media1.giphy.com/media/IhO6ksgdk31JxbbFLA/200w.gif?cid=82a1493bmbpukqu53l1t49epgeet5ftpueaao9zhf2a6szbn&rid=200w.gif&ct=g)
