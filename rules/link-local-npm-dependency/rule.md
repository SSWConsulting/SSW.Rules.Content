---
type: rule
title: Do you know how to link local dependency for npm?
seoDescription: Master the 3 ways of local npm dependency management with SSW's expert guide. 
uri: link-local-npm-dependency
authors:
  - title: Thom Wang
    url: https://ssw.com.au/people/thom-wang
created: 2025-02-20T10:51:21.000Z
archivedreason: null
guid: fef36fc2-3d09-4582-83de-80719a0042e4
---

When working on multiple related JavaScript projects, you may need to test changes in a local dependency without publishing it to npm. `npm link` provides a way to symlink a local package, allowing real-time updates without reinstalling the package manually. However, improper usage can lead to issues like dependency mismatches or unresolved modules.

<!--endintro-->

## How `npm link` works

`npm link` creates a symbolic link between a globally registered local package and a project that depends on it.

### Steps to link a local dependency

1. Navigate to the local package directory (the dependency you are developing) and run:

  ```sh
  npm link
  ```

   This registers the package globally on your system.

2. Navigate to the project that will use this dependency and run:

  ```sh
  npm link <package-name>
  ```

   This links the globally registered package into your project’s `node_modules`.

### Example usage

If you're developing `my-local-package` and want to use it in another project:

```sh
cd ~/projects/my-local-package
npm link
cd ~/projects/my-app
npm link my-local-package
```

Now, `my-app` will use the local version of `my-local-package` instead of fetching it from npm.

## Common issues and fixes

* **Module Resolution Issues**: If your project uses a different version of a peer dependency than the linked package, you might get errors. A common fix is running:
  
```sh
npm install
```
  
  in both the linked package and the main project.

* **TypeScript Not Detecting Changes**: Sometimes, TypeScript may not immediately recognize changes in a linked package. Restarting the TypeScript server (`tsc --watch`) or adding `"preserveSymlinks": true` in `tsconfig.json` can help.

## Alternatives to `npm link`

### 1. Using `npm install <path>`

Instead of linking, you can install a local package directly:

```sh
npm install ../my-local-package
```

::: good
Figure: Good example - Simpler alternative that avoids symlink-related issues
:::

### 2. Using `npm pack`

Another option is to create a tarball of the package and install it manually:

```sh
cd my-local-package
npm pack
npm install ../my-local-package/my-local-package-1.0.0.tgz
```

::: good
Figure: Good example - Simulates a real npm package installation
:::

## Best practices

* Use `npm link` mainly for development, not for production environments
* Always verify dependencies are correctly installed after linking
* Consider `npm install <path>` or `npm pack` if `npm link` causes issues

By understanding and properly using `npm link`, you can streamline local package development while avoiding common pitfalls.
