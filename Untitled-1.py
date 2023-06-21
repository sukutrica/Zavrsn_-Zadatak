print("Dragan")
print("Dusan")


PS C:\Users\danil\OneDrive\Desktop\Proba> git clone https://github.com/sukutrica/Zavrsn_-Zadatak.git
Cloning into 'Zavrsn_-Zadatak'...
remote: Enumerating objects: 55, done.
Receiving objects: 100% (55/55), 71.75 MiB | 863.00 KiB/s, done.
Resolving deltas: 100% (24/24), done.
PS C:\Users\danil\OneDrive\Desktop\Proba> git status
fatal: not a git repository (or any of the parent directories): .git
PS C:\Users\danil\OneDrive\Desktop\Proba> cd zavrsn_-Zadatak
PS C:\Users\danil\OneDrive\Desktop\Proba\zavrsn_-Zadatak> git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        Untitled-1.py

nothing added to commit but untracked files present (use "git add" to track)
PS C:\Users\danil\OneDrive\Desktop\Proba\zavrsn_-Zadatak> git status
On branch main

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   Untitled-1.py

PS C:\Users\danil\OneDrive\Desktop\Proba\zavrsn_-Zadatak> git commit -m "Added new file"
Author identity unknown
*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'danil@DESKTOP-AMNDFMK.(none)')
PS C:\Users\danil\OneDrive\Desktop\Proba\zavrsn_-Zadatak> git push origin main
info: please complete authentication in your browser...

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   Untitled-1.py

PS C:\Users\danil\OneDrive\Desktop\Proba\zavrsn_-Zadatak> git commit -m "added new file"
Author identity unknown

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'danil@DESKTOP-AMNDFMK.(none)')
PS C:\Users\danil\OneDrive\Desktop\Proba\zavrsn_-Zadatak> git config --global user.email"danilovic.dragan.1976@gmail.com"
PS C:\Users\danil\OneDrive\Desktop\Proba\zavrsn_-Zadatak> git config --global user.name "sukutrica"
PS C:\Users\danil\OneDrive\Desktop\Proba\zavrsn_-Zadatak> git add .
PS C:\Users\danil\OneDrive\Desktop\Proba\zavrsn_-Zadatak> git commit -m "added"
Author identity unknown

*** Please tell me who you are.

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'danil@DESKTOP-AMNDFMK.(none)')
PS C:\Users\danil\OneDrive\Desktop\Proba\zavrsn_-Zadatak> git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)

PS C:\Users\danil\OneDrive\Desktop\Proba\zavrsn_-Zadatak> git add .
PS C:\Users\danil\OneDrive\Desktop\Proba\zavrsn_-Zadatak> git commit -m "ccc"
Author identity unknown

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'danil@DESKTOP-AMNDFMK.(none)')
PS C:\Users\danil\OneDrive\Desktop\Proba\zavrsn_-Zadatak> git config user.name "sukutrica"
PS C:\Users\danil\OneDrive\Desktop\Proba\zavrsn_-Zadatak> git config user.email "danilovic.dragan.1976@gmail.com"
PS C:\Users\danil\OneDrive\Desktop\Proba\zavrsn_-Zadatak> git commit -m "added"
[main 855e768] added
 1 file changed, 2 insertions(+)
 create mode 100644 Untitled-1.py
PS C:\Users\danil\OneDrive\Desktop\Proba\zavrsn_-Zadatak> git push origin main
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 4 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 302 bytes | 151.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/sukutrica/Zavrsn_-Zadatak.git
   c48be62..855e768  main -> main
PS C:\Users\danil\OneDrive\Desktop\Proba\zavrsn_-Zadatak>
