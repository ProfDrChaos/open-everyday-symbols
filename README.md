License: LaTeX Project Public License 1.3c

Maintainer: Pascal Bercher, pascal.bercher@anu.edu.au

Please read the documentation (PDF) for instructions. 

In a nutshell, this package is an open and continuously extended list of “everyday symbols” (i.e., not of a mathematical or otherwise primarily technical nature). I call it open because I ask everybody to contribute your own symbols to it. I hope that enough people consider creating their own symbols, e.g., with the help of chatGPT, and contribute them to this package.

A few notes in case you want to contribute:
- Check out the repository that's linked from CTAN, make the respective changes, and make a pull request. Ideally, drop me an email as well so that I won't miss it. You can also drop me an email pro-actively before the request, especially if you have questions or suggestions for improvement that might warrant discussion.
- I request that you use/implement the "main command" \everydaySymbol[options]{main-category}{sub-identifier-number}, i.e., options can be any key-value pair you set up, main-category is a descriptive *main category*, such as door, car, or whatever. *sub-identifier* is a specialization of that as it might be that several authors contribute to the same main category; this keeps it sorted. I would like to request to have a combination of a more descriptive subcategory plus an author name or ID (since even the sub category might not be unique, think of generic ones like "cartoony" or "simple", of which there might be many for the same main category; adding the author will keep this clean). *number* is a number for the individual command, from 01 counting upwards (three digits if you have at least 3; we might define aliases to eliminate leading zeros; not done yet). In a nutshell: Just follow the existing examples.
- Note that the actual sources of the project are organized in subfolders and individual files. They are combined into one (for CTAN) using a script. So, please check out the repository before you make any changes.
- If you have enough time, consider making them modular using additional keys, to allow people to configure the graphics further and thus create additional variants.

Finally, let me tell you that creating graphics using chatGPT may actually be quite fun. :)