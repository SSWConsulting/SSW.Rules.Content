---
type: rule
title: Do you format and comment your regular expressions?
uri: format-and-comment-regular-expressions
authors:
  - title: Igor Goldobin
    url: https://ssw.com.au/people/alumni/igor-goldobin
created: 2024-03-09T01:22:57.845Z
guid: d9f9c7e3-0687-4760-9129-a7178d2f45f6

---

Regular expressions are a very powerful tool for pattern matching, but a complicated regex can be very difficult for a human to read and to comprehend. That is why, like any good code, a good regular expression must be well formatted and documented.

<!--endintro-->

Here are some guidelines when formatting and documenting your regex:

- Keep each line under 80 characters, horizontal scrolling reduces readability
- Break long patterns into multiple lines, usually after a space or a line break
- Indent bracers to help think in the right scope
- Format complicated OR patterns into multiple blocks like a case statement
- Comment your regex on what it does, don't just translate it into English

```regex

# Match <BODY
<BODY
# Match any non > char for zero to infinite number of times
[^>]*
# MATCH >
>
```

::: bad
Bad example: Comment that translates the regex into English
:::

```regex
# Match the BODY tag
<BODY
# Match any character in the body tag
[^>]*
# Match the end BODY tag
>
```

::: good
Good example: Comment that explains the purpose of the pattern
:::

```regex
(?six-mn:(Label|TextBox)\s+(?<Name>\w+).*(?<Result>\k<Name>\.TextAlign\s*=\s* ((System\.)?Drawing\.)?ContentAlignment\.(?! TopLeft|MiddleLeft|TopCenter|MiddleCenter)\w*)(?!(?<=\k<Name>\.Image.*)|(?
=.*\k<Name>\.Image)))
```

::: bad
Bad example: Pray you never have to modify this regex
:::


```regex
(?six-mn:
    # Match for Label or TextBox control
    # Store name into <name> group
    (Label|TextBox)\s+(?<Name>\w+).*

    # Match any non-standard TextAlign
    # Store any match in Result group for error reporting in CA
    (?<Result>
        # Match for control's TextAlign Property
        \k<Name>\.TextAlign\s*=\s*

        # Match for possible namespace
        ((System\.)?Drawing\.)?ContentAlignment\.

        # Match any ContentAlignment that is not in the group
        (?!TopLeft|MiddleLeft|TopCenter|MiddleCenter)\w*
    )

    # Skip any Control that has image on it
    (?!
        (?<=
            \k<Name>\.Image
            .*
        )
    |
        (?=
            .*
            \k<Name>\.Image
        )
    )
)
```

::: good
Good example: Now it make sense!
:::
