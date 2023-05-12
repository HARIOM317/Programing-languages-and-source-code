/*
  Symbol object is used to specify an operator or identifier declared in a Dart programming language. Generally, we do not need to use symbols while Dart programming, but they are helpful for APIs. It usually refers to identifiers by name, because identifier names can vary but not identifier symbols.
 */

import 'dart:mirrors';

void main(List<String> args) {
  Symbol symbol = new Symbol("HsR");
  // convert symbol to string
  String name = MirrorSystem.getName(symbol);
  print(name);
}
