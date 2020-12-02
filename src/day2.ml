let day = "2"


let get_index_list x list =
  let rec aux x list i = match list with
    | [] -> failwith "Not Found"
    | y :: ys -> if y = x then i else aux x ys (i + 1)
  in
  aux x list 0
;;

(* String.get string n   returns the character at index 'n' in string 'string'. *)
(* String.index s c      returns the index of the first occurrence of character c in string s. *)

let string_of_char c = String.make 1 c

(* let reverse list =
    let rec aux acc = function
      | [] -> acc
      | x :: xs -> aux (x :: acc) xs
    in
    aux [] list
;; *)

(* let make_range_list a b =
  let rec aux acc a b =
    if a > b then acc
    else if a < b then aux (a :: acc) (a + 1) b
    else (* if a = b then *) a :: acc
  in
  List.map string_of_int (reverse (aux [] a b))
;; *)

(* https://stackoverflow.com/questions/10068713/string-to-list-of-char *)
let explode s = (* string to char list *)
  let rec exp i l =
    if i < 0 then l else exp (i - 1) (s.[i] :: l) in
  exp (String.length s - 1) []
;;

let make_tuples list =
  let rec aux acc = function
    | [] -> acc
    | x :: xs ->
      (* String.sub : string -> int -> int -> string *)  (* slice ampak druga stevilka je dolzina *)
      let num1 = String.sub x 0 ((String.index x '-')) in
      let num2 = String.sub x ((String.index x '-') + 1) ((String.index x ' ') - (String.index x '-') - 1) in
      let crka = string_of_char (String.get x ((String.index x ':') - 1)) in
      let geslo = String.sub x ((String.index x ':') + 2) (String.length x - (String.index x ' ') - 4) in
      let tup = (num1, num2, crka, geslo) in
      aux (tup :: acc) xs
  in
  aux [] list
;;

let rec ponovitve x list counter = (* list = explode niz *)
    match list with
    | [] -> counter
    | y :: ys ->
      if x = string_of_char y then ponovitve x ys (counter + 1)
      else ponovitve x ys counter
;;

let rec prestej_dobre list counter =
    let ok (a, b, c, d) =
      let ponovitev = ponovitve c (explode d) 0 in
      if ponovitev >= int_of_string a && ponovitev <= int_of_string b then true
      else false
    in
    match list with
    | [] -> counter
    | tup :: tups -> if ok tup then prestej_dobre tups (counter + 1) else prestej_dobre tups counter
;;


let naloga1 vsebina_datoteke =
  let input_list = String.split_on_char '\n' (String.trim vsebina_datoteke) in
  (* "3-14 v: nekogeslovvv" *)

  let tuple_list = make_tuples input_list in
  (* ("3", "14", "v", "nekogeslovvv") *)

  let solution = string_of_int (prestej_dobre tuple_list 0) in
  
  print_endline ("day " ^ day ^ ", puzzle 1: " ^ solution);
  solution
;;


let ok2 (st1, st2, crka, niz) =
  if (crka = string_of_char (String.get niz ((int_of_string st1) - 1))) && (crka = string_of_char (String.get niz ((int_of_string st2) - 1)))
    then false
  else if (crka = string_of_char (String.get niz ((int_of_string st1) - 1))) || (crka = string_of_char (String.get niz ((int_of_string st2) - 1)))
    then true
  else false
;;

let rec prestej_dobre_2 list counter =
  match list with
  | [] -> counter
  | tup :: tups -> if ok2 tup then prestej_dobre_2 tups (counter + 1) else prestej_dobre_2 tups counter
;;


let naloga2 vsebina_datoteke =
  let input_list = String.split_on_char '\n' (String.trim vsebina_datoteke) in
  let tuple_list = make_tuples input_list in
  (* ("3", "14", "v", "nekogeslovvv") *)
  
  let solution = string_of_int (prestej_dobre_2 tuple_list 0) in

  print_endline ("day " ^ day ^ ", puzzle 2: " ^ solution);
  solution
;;

(* Celoten dan 2 je bil napisan na način "kako pretvorit imperativne pythonske ukaze v ocaml"... ojoj *)

let _ =
  let preberi_datoteko ime_datoteke =
    let chan = open_in ime_datoteke in
    let vsebina = really_input_string chan (in_channel_length chan) in
    close_in chan;
    vsebina
  and izpisi_datoteko ime_datoteke vsebina =
    let chan = open_out ime_datoteke in
    output_string chan vsebina;
    close_out chan
  in

  let vsebina_datoteke = preberi_datoteko ("data/day_" ^ day ^ ".in") in
  let odgovor1 = naloga1 vsebina_datoteke
  and odgovor2 = naloga2 vsebina_datoteke
  in

  izpisi_datoteko ("out/day_" ^ day ^ "_1.out") odgovor1;
  izpisi_datoteko ("out/day_" ^ day ^ "_2.out") odgovor2
;;