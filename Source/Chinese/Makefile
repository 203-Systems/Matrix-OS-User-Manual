# Define source and build directories
SRCDIR := $(subst /,\,$(CURDIR))
BUILDDIR := $(subst \Source\,\PDF\,$(SRCDIR))

# Find all the .md files under the source directory
SRCS := $(shell dir /s /b $(SRCDIR)\*.md)

# Generate PDF paths for each source file
PDFS := $(patsubst $(SRCDIR)%.md,$(BUILDDIR)%.pdf,$(SRCS))

DATE := $(shell powershell -Command "Get-Date -format 'yyyy-MM-dd'")
GITTAG := $(shell git describe --tags --abbrev=0)

PARAM := $(shell type param.txt)

$(info $(SRCDIR))
$(info $(BUILDDIR))
$(info SRCS: $(SRCS))
$(info PDFS: $(PDFS))

$(info DATE: $(DATE))
$(info TAG: $(GITTAG))

$(info PARAM: $(PARAM))

# Rule to build all PDFs
all: clean $(PDFS)

# Rule to build a PDF from a source file
$(BUILDDIR)%.pdf: $(SRCDIR)%.md
	@if not exist $(dir $@) (mkdir $(dir $@))
	@echo Building $@ from $<
	@pandoc $< -o $@ --from markdown --template "../../Template/eisvogel.tex" --listings --top-level-division=section  -V date="$(DATE)" -V git_tag="$(GITTAG)" $(PARAM)

# Clean rule to remove all PDFs
clean:
	@echo Cleaning $(BUILDDIR)
	@del /S /F /Q $(BUILDDIR)
