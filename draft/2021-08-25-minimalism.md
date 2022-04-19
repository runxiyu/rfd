---
layout: post
author: Andrew Yu
title: Minimalism
---

The world depends on computers. Computers help us complete daily tasks such as typesetting, fetching information, et cetera.

In the COVID-19 pandemic, computers help people work from home, which prevented the economy from going into a full-blown stall. As a middle school student, I saw the department of education of Shanghai hire teachers to record lectures which get distributed over TV and the Internet. Schools use meeting software, such as Tencent Meetings, to teach students at home. If it wasn’t for the Internet, so many people would have lost jobs, and society would be inoperative.

Most of the software people use these days are Proprietary Software—nobody except the copyright holder and specially authorized people are allowed to edit the program to their needs, audit how the program runs, etc.

Note that, in this document, free always refers to freedom, rather than price, unless otherwise specified.

LaTeX was used to typeset this document (the original version, not the webpage). I argue that LaTeX, though a sophisticated, free and high-quality typesetting system, is poorly optimized. For example, to get cross references right, LaTeX has to compile the document twice. The first time it compiles the document, recording all cross references. The second time is when it actually writes the correct cross reference numbers into the output. Compiling two times is redundant—it makes sense to go through the cross references twice to get them right, but it is utterly unnecessary to compile and produce output twice. Counting references is a fast task, but when it’s mixed up with producing output, a slow task, the overall speed decreases dramatically.

LaTeX is built on TeX, which sadly is designed with typesetters in mind, not authors or book designers. To have (good, sane and needed) things like cross references, maybe we need something that’s not just a macro set based on a typesetting engine. However, I believe that a feature like implementing cross references shouldn’t just be confined to LaTeX, TeX and typesetting—it has use-cases in other places, for example, giving cross references in plain text documents.

Do one thing, and do it well.
There ought to be a program, to just handle your cross references, in a standard way. It does string manipulation with a tool like sed, which replaces the \refs with the correct number, and removes the \labels. Ideally, this utility should allow the user to choose which patterns to use as the label and reference commands, since this general-prpose utility should be designed to cover general use-cases.

This goes similarly for other utilities, of course. Converting TeX code to HTML, sending strings to IRC, you name it. We don’t want every GUI program to have it’s own emoji picker. We want one for the whole system. Furthermore, we don’t want to write a menu system just for the emoji picker. We want a general menu system, such as dmenu. The Suckless people make good software that mostly adheres to this principles, and many of the below.

Use standard pipes.
To be specific, use standard input/output for general utilities and FIFO pipes for background daemons and other things like window managers.

(To be continued)
