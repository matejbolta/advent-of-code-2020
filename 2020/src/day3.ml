let day = "3"
(*
Današnja rešitev mi je zelo všeč in se mi zdi veliko boljša kot včerajšnja.
Potek je veliko bolj splošen in "funkcijski"
*)

let list_index list char = (* list_index : 'a list -> 'a -> int *)
  let rec aux list char counter = match list with
    | [] -> failwith "Oh dear santa"
    | x :: xs -> if (x = char) then counter else aux xs char (counter + 1)
  in
  aux list char 0
;;

let count_trees right_step down_step list = (* int -> int -> string list -> int *)
  let rec count_trees_aux tree_counter latitude longitude right_step down_step = function
    | [] -> tree_counter
    | row :: rows when (list_index list row) mod down_step = 0 -> (* Smo v primeru, ki ga korak down_step NE preskoči *)
      if String.get row (latitude mod (String.length row)) = '#' then  (* String.get : string -> int -> char *)
        count_trees_aux (tree_counter + 1) (latitude + right_step) (longitude + 1) right_step down_step rows
      else
        count_trees_aux tree_counter (latitude + right_step) (longitude + 1) right_step down_step rows
    | _ :: rows -> (* Se izvede v primeru, da smo v vrstici, ki jo korak down_step preskoči *)
      count_trees_aux tree_counter latitude (longitude + 1) right_step down_step rows
  in
  count_trees_aux 0 0 0 right_step down_step list
;;

let naloga1 vsebina_datoteke =
  let s = vsebina_datoteke
    |> String.trim
    |> String.split_on_char '\n'
    |> count_trees 3 1
    |> string_of_int
  in
  print_endline ("day " ^ day ^ ", puzzle 1: " ^ s);
  s
;;

let naloga2 vsebina_datoteke =
  let s =
    List.map
      (fun (r, d) ->
        vsebina_datoteke
        |> String.trim
        |> String.split_on_char '\n'
        |> count_trees r d)
      [(1, 1); (3, 1); (5, 1); (7, 1); (1, 2)]
    |> List.fold_left ( * ) 1
    |> string_of_int
  in
  print_endline ("day " ^ day ^ ", puzzle 2: " ^ s);
  s
;;

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

  let vsebina_datoteke = preberi_datoteko ("2020/data/day_" ^ day ^ ".in") in
  let odgovor1 = naloga1 vsebina_datoteke
  and odgovor2 = naloga2 vsebina_datoteke
  in

  izpisi_datoteko ("2020/out/day_" ^ day ^ "_1.out") odgovor1;
  izpisi_datoteko ("2020/out/day_" ^ day ^ "_2.out") odgovor2
;;